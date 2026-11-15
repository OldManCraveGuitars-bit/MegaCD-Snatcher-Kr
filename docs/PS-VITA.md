# PS Vita 전용 코어 시험판 — V1.02

**V1.02 r62 PS Vita 전용 `.self`입니다. ACT1→ACT2 연속 진행 시 보이스 자막이 사라지는 코어 오류를 수정했습니다. 빌드·정적 검사는 통과했지만, 실제 비타에서 부팅·음성·자막·속도를 확인한 배포판은 아닙니다.** Windows 패처에는 포함되지 않으므로 별도로 받습니다. **V1.01 게임은 그대로 사용하고 코어만 교체하세요.**

[V1.02 Vita 시험판 다운로드](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/releases/tag/v1.02-vita-test1) · [V1.02 게임 패처](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/releases/tag/v1.02)

## 필요한 파일

- RetroArch가 이미 실행되는 PS Vita. 이 코어에 포함된 프런트엔드는 **RetroArch 1.22.2 일반 Vita 빌드**이며 Piglet 빌드가 아닙니다. 다른 버전·배포판 조합은 확인하지 않았습니다.
- `Snatcher-KR-V1.02-Vita-test1.zip`의 `genesis_plus_gx_snatcher_kr_libretro.self`와 같은 이름의 `.info`.
- V1.02 패처로 만든 `Snatcher-KR-v1.02.bin`과 `Snatcher-KR-v1.02.cue`. **기존 V1.01 BIN/CUE도 동일한 게임이므로 그대로 사용**합니다. V1.0 이하는 원본에서 최신 게임 패치를 적용하세요.
- 사용자가 보유한 미국판 Sega CD BIOS `bios_CD_U.bin`.

## 설치와 실행

1. RetroArch를 종료합니다. 기존 게임 저장과 `ux0:/data/retroarch/retroarch.cfg`는 먼저 보관합니다.
2. PC에서 Vita 시험판 ZIP을 풀고 VitaShell의 USB/FTP 등을 이용해 파일을 복사합니다.

   | ZIP 안의 파일 | 일반 설치 기준 목적지 |
   | --- | --- |
   | `genesis_plus_gx_snatcher_kr_libretro.self` | `ux0:/app/RETROARCH/genesis_plus_gx_snatcher_kr_libretro.self` |
   | `genesis_plus_gx_snatcher_kr_libretro.info` | `ux0:/app/RETROARCH/info/genesis_plus_gx_snatcher_kr_libretro.info` |

   위 경로는 RetroArch 1.22.2 소스의 `app0:/` 및 `app0:/info` 기본값을 기준으로 합니다. **설정 → 디렉터리**에서 코어 정보 위치를 바꾼 경우 `.info`는 그 위치에 넣습니다. `.self`는 기존 `genesis_plus_gx_libretro.self`와 같은 폴더에 추가합니다. 기존 일반 코어나 `eboot.bin`을 덮어쓰지 않습니다.
3. BIOS를 설정된 **시스템/BIOS** 폴더에 넣습니다. 일반 설치 기본 경로는 `ux0:/data/retroarch/system/bios_CD_U.bin`입니다.
4. 패치한 BIN과 CUE를 같은 게임 폴더에 복사합니다. 예: `ux0:/data/roms/snatcher/`. CUE에서 참조하는 BIN 이름을 그대로 유지합니다.
5. RetroArch에서 **코어 불러오기 → Sega CD - Genesis Plus GX (Snatcher KR V1.02 Vita test1)**을 선택합니다. 정보 파일이 인식되지 않으면 `genesis_plus_gx_snatcher_kr_libretro.self`라는 파일명을 확인합니다. 이전 Vita 시험판을 사용했다면 전용 SELF와 INFO를 모두 교체합니다.
6. **콘텐츠 불러오기**에서 `Snatcher-KR-v1.02.cue` 또는 기존 V1.01 CUE를 선택합니다. BIN을 직접 열면 CD 음성 트랙 구성이 올바르게 전달되지 않을 수 있습니다.
7. RetroArch를 완전히 재시작하고, 기존 세이브스테이트 대신 게임을 새로 시작하거나 **게임 내 저장**을 불러옵니다. 오프닝의 음성과 한국어 자막 표시를 확인합니다. 이전 세이브스테이트의 호환성을 보증하지는 않습니다.

일반 코어로 돌아가려면 기존 `genesis_plus_gx_libretro.self`를 선택합니다. 삭제할 경우 이번에 추가한 전용 `.self`와 `.info`만 제거하면 됩니다.

## 무엇을 확인했나

- Windows·Android·Linux와 동일한 **r62 코어 소스**를 ARM Vita 대상으로 컴파일하고 RetroArch 1.22.2와 정적으로 링크했습니다. ACT2 CD 음성의 실제 자막 구간에서 지난 PCM 상태를 비우는 수정이 포함됩니다. DLL/SO의 확장자를 바꾼 파일이 아닙니다.
- ARM 32비트 ELF, 필요한 코어·자막 함수 6개, 생성된 SELF 컨테이너를 검사했습니다.
- 최종 ELF에 **자막 비트맵 은행 33/33개**가 V1.0 원본과 정확히 같은 바이트로 들어가는지 검사했습니다. 추가 CD 음성 자막 **431쪽**도 포함됩니다.
- 실제 비타에서 코어 선택·게임 부팅·소리·표시·속도·저장 호환성은 아직 확인하지 않았습니다. PC용 기존 스크린샷을 비타 실행 증거로 사용하지 않습니다.

문제가 있으면 RetroArch 버전, 일반/Piglet 여부, 코어 선택 직후인지 게임 로딩 후인지, 오류 화면과 장면을 알려 주세요. 게임과 BIOS 파일은 보내지 않아도 됩니다.

## 해시와 재빌드

릴리스의 `SHA256SUMS-Vita-v1.02-test1.txt`는 SELF·설치 ZIP·소스 압축파일·빌드 명세의 SHA-256입니다. `BUILD-VITA.json`에는 빌드 커밋, Actions 주소, 컴파일된 ELF와 자막 은행별 해시, 수정 overlay 해시 및 미검증 항목이 기록됩니다.

- 코어 입력 ZIP SHA-256: `58b49adcbb6bfe9bd3595e42866968053ccd7f9755d31bbae1588fc722c95741`
- 수정 overlay SHA-256: `30d8dd841a9b7f815a6c2188cd964f961433d5e6fb947c242c1c4bf8ccdb7f2e`
- 자막 헤더 SHA-256: `adf5a4c792801fb917ace5af6e2ad0cb4165f96dddee09222efb025ef4e875ad`
- RetroArch 소스: `v1.22.2`, 커밋 `69a4f0ea1e8aaf442ae4858f2e7f2b31a1776576`
- 프런트엔드 수정: Vita2D 메뉴 행렬 전달 시 구조체 포인터 대신 내부 `float` 배열을 전달하는 타입 오류 1곳을 교정했습니다. GCC 15 호환 수정이며 소스 묶음의 `RETROARCH-CHANGES.patch`에 기록합니다.
- 코어 빌드 옵션: `-Dcrc32=snatcher_kr_crc32`로 코어의 기존 CRC 함수와 호출 이름을 구분해 RetroArch의 zlib와 정적 링크할 때 생기는 중복을 해결합니다. CRC 계산 구현은 유지됩니다.
- V1.01/V1.02 게임 BIN SHA-256: `dd91fc991ab5e7feb0c965cc15e001d9c0ff6dc24e7b504293b51dec6447381f`

`Snatcher-KR-V1.02-Vita-source.tar.xz`에 해당 RetroArch 소스 전체, r62 코어 소스 ZIP, 빌드 스크립트와 명세를 제공합니다. 원본 저작권·라이선스 고지는 각 소스에 보존됩니다. 실행 ZIP에도 코어·RetroArch·Galmuri 라이선스를 동봉합니다. 게임·BIOS·VPK는 포함하지 않습니다.

공개 저장소 루트에서 다음과 같이 재빌드합니다. Linux의 Docker가 필요하며, 사용한 VitaSDK 이미지는 digest로 고정했습니다.

```sh
docker run --rm -v "$PWD:/workspace" -w /workspace \
  vitasdk/vitasdk@sha256:7f5eee50ff95b73c8c847dbfef6227aa0035886444b4d0254c21da8369ff1efc \
  bash tools/build_vita.sh
```

새 출력은 `vita-out/`에 생성됩니다. 기존 `vita-build/`가 있으면 먼저 다른 위치로 옮겨 빈 작업 위치에서 실행합니다. 도구·코어·프런트엔드의 버전을 고정했지만 파일 시각 등으로 SELF 해시가 매번 완전히 같다는 재현성 검증은 하지 않았습니다.

구조 참고: [Libretro의 Vita 정적 링크 설명](https://docs.libretro.com/development/retroarch/compilation/psvita/), [VitaSDK](https://vitasdk.org/), [RetroArch 1.22.2 기본 경로 소스](https://github.com/libretro/RetroArch/blob/v1.22.2/frontend/drivers/platform_psp.c).
