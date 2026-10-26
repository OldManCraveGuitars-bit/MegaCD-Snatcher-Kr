"""Fail the build on wrong architecture, missing hooks or stale caption banks.

This is a build/static inspection, not a claim of Vita runtime compatibility.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess

ROOT = Path.cwd()
CORE = ROOT / 'vita-build/core'
RA = ROOT / 'vita-build/RetroArch'
OUT = ROOT / 'vita-out'
HEADER_SHA = 'adf5a4c792801fb917ace5af6e2ad0cb4165f96dddee09222efb025ef4e875ad'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    header = (CORE / 'core/kr_host_caption_assets.h').read_bytes()
    assert sha(header) == HEADER_SHA, 'caption source changed'
    banks = {
        name.decode(): bytes(int(v, 16) for v in re.findall(rb'0x([0-9a-fA-F]{2})', body))
        for name, body in re.findall(
            rb'static const unsigned char (\w+)\[\] = \{\n(.*?)\n\};', header, re.S)
    }
    banks = {name: data for name, data in banks.items() if len(data) >= 960}
    assert len(banks) == 33, len(banks)
    assert len(banks['kr_extra_cdda_pixels']) == 431 * 960
    elf_path = RA / 'retroarch_vita.elf.unstripped.elf'
    elf = elf_path.read_bytes()
    assert elf[:6] == b'\x7fELF\x01\x01', 'not ELF32 little endian'
    assert struct.unpack_from('<H', elf, 18)[0] == 40, 'not ARM'
    flags = struct.unpack_from('<I', elf, 36)[0]
    symbols = subprocess.check_output(['arm-vita-eabi-nm', str(elf_path)], text=True)
    required = ['retro_init', 'retro_run', 'retro_load_game', 'retro_api_version',
                'kr_host_caption_begin_frame', 'kr_host_ending_quote_finalize_frame']
    for symbol in required:
        assert re.search(r'\b' + symbol + r'$', symbols, re.M), symbol
    for name, data in banks.items():
        assert data in elf, f'missing or changed caption bank: {name}'
    source_self = RA / 'retroarch_vita.self'
    self_data = source_self.read_bytes()
    assert self_data[:4] == b'SCE\x00', 'not a SELF container'
    assert len(self_data) > 1_000_000, 'unexpectedly small SELF'
    output = OUT / 'genesis_plus_gx_snatcher_kr_libretro.self'
    shutil.copy2(source_self, output)
    build = {
        'version': 'V1.0-Vita-test1', 'status': 'build_and_static_checks_passed',
        'vita_hardware_tested': False, 'vita_emulator_tested': False,
        'gameplay_verified': False, 'frame_rate_verified': False,
        'core_source_sha256': os.environ['CORE_SHA'],
        'caption_header_sha256': HEADER_SHA,
        'retroarch_tag': 'v1.22.2', 'retroarch_commit': os.environ['RA_COMMIT'],
        'retroarch_patch': 'tools/retroarch-vita-gcc15.patch',
        'retroarch_patch_sha256': sha((ROOT / 'tools/retroarch-vita-gcc15.patch').read_bytes()),
        'sdk_image': os.environ['SDK_IMAGE'],
        'build_commit': os.environ.get('GITHUB_SHA'),
        'workflow_run': '{}/{}/actions/runs/{}'.format(
            os.environ.get('GITHUB_SERVER_URL', 'https://github.com'),
            os.environ.get('GITHUB_REPOSITORY', ''), os.environ.get('GITHUB_RUN_ID', '')),
        'architecture': 'ELF32 little-endian ARM', 'elf_flags': hex(flags),
        'elf_sha256': sha(elf), 'required_symbols': required,
        'caption_banks': {name: {'bytes': len(data), 'sha256': sha(data)}
                          for name, data in banks.items()},
        'caption_banks_verified': len(banks), 'extra_cdda_pages': 431,
        'file': output.name, 'bytes': len(self_data), 'sha256': sha(self_data),
    }
    (OUT / 'BUILD-VITA.json').write_text(json.dumps(build, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: build[k] for k in ['status', 'bytes', 'sha256', 'caption_banks_verified']}))


if __name__ == '__main__':
    main()
