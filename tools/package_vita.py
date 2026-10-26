"""Package a downloaded, successful Vita build without ROM or BIOS inputs."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tarfile
import zipfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('build', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    report_path = args.build / 'BUILD-VITA.json'
    report = json.loads(report_path.read_text(encoding='utf-8'))
    assert report['status'] == 'build_and_static_checks_passed'
    assert report['caption_banks_verified'] == 33
    assert report['vita_hardware_tested'] is False
    binary = args.build / 'genesis_plus_gx_snatcher_kr_libretro.self'
    assert digest(binary) == report['sha256']
    source = args.build / 'Snatcher-KR-V1.0-Vita-source.tar.xz'
    # Check downloaded files against the checksums made by the build runner.
    for line in (args.build / 'SHA256SUMS-build.txt').read_text().splitlines():
        expected, name = line.split(maxsplit=1)
        assert digest(args.build / Path(name).name) == expected
    with tarfile.open(source) as archive:
        members = {m.name.removeprefix('./'): m for m in archive.getmembers()}
        assert 'RetroArch/Makefile.vita' in members
        assert 'modified-core-source.zip' in members
        license_data = archive.extractfile(members['RetroArch/COPYING']).read()
        embedded_report = archive.extractfile(members['BUILD-VITA.json']).read()
        assert json.loads(embedded_report) == report
        notices = {}
        for name, member in members.items():
            leaf = Path(name).name.upper()
            if (member.isfile() and name.startswith('RetroArch/')
                    and leaf.startswith(('LICENSE', 'COPYING', 'COPYRIGHT'))):
                notices['licenses/' + name] = archive.extractfile(member).read()
    args.output.mkdir(parents=True, exist_ok=False)
    for path in (binary, source, report_path):
        shutil.copy2(path, args.output / path.name)
    contents = {
        binary.name: binary.read_bytes(),
        'genesis_plus_gx_snatcher_kr_libretro.info': (repo / 'docs/genesis_plus_gx_snatcher_kr_libretro.info').read_bytes(),
        'README-KO.md': (repo / 'docs/PS-VITA.md').read_bytes(),
        'BUILD-VITA.json': report_path.read_bytes(),
        'licenses/RetroArch-COPYING.txt': license_data,
        'licenses/CORE-LICENSE.txt': (repo / 'licenses/CORE-LICENSE.txt').read_bytes(),
        'licenses/Galmuri-OFL-1.1.txt': (repo / 'licenses/Galmuri-OFL-1.1.txt').read_bytes(),
    }
    contents.update(notices)
    for path in sorted((args.build / 'licenses').rglob('*')):
        if path.is_file():
            contents[path.relative_to(args.build).as_posix()] = path.read_bytes()
    zip_path = args.output / 'Snatcher-KR-V1.0-Vita-test1.zip'
    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in contents.items():
            archive.writestr(name, data)
    with zipfile.ZipFile(zip_path) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(contents)
        for name, data in contents.items():
            assert archive.read(name) == data
    sums = ''.join(f'{digest(path)}  {path.name}\n' for path in sorted(args.output.iterdir()))
    (args.output / 'SHA256SUMS-Vita-test1.txt').write_text(sums, encoding='utf-8')
    print(json.dumps({'packaged': len(contents), 'assets': 5, 'output': str(args.output)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
