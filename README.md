# MegaCD-Snatcher-Kr — v0.75 시험판

메가 CD 미국판 *Snatcher*의 한국어 패치입니다. 게임 속 문구·선택문뿐 아니라 **음성에 맞춰 표시되는 한국어 자막**을 중점적으로 다룹니다. 자막은 게임의 페이지 넘김과 별도로 음성 진행을 따르도록 만든 **전용 Genesis Plus GX 코어**에서 그립니다. 화면 아래쪽의 흰 글자·검은 테두리 방식이며, 별도의 큰 검은 자막 상자를 만드는 방식이 아닙니다.

> **중요: 일반 Genesis Plus GX 코어만으로는 보이스 자막이 나오지 않습니다.** 이 배포판과 짝을 이루는 개조 코어를 반드시 사용하세요. 게임 BIN만 패치한 뒤 기본 코어에서 실행하는 것은 지원하는 완성 구성으로 간주하지 않습니다.

이 저장소와 배포 파일에는 원본 게임 이미지, 패치 완료된 전체 게임 이미지, BIOS, RetroArch APK가 없습니다. 본인이 보유한 정확한 미국판 BIN과 별도 BIOS가 필요합니다. 비공식·비상업적 팬 프로젝트이며 Konami, Sega, Libretro와 제휴하지 않았습니다. **v0.75는 시험판**입니다. 전편 플레이·모든 번역 문장·모든 기기 조합을 최종 승인한 판으로 주장하지 않습니다.

## 화면 예시

| 화면 | 설명 |
| --- | --- |
| ![타이틀 화면](docs/screenshots/title-r249.png) | r249 게임의 타이틀. 원작의 타이틀 연출은 유지됩니다. |
| ![한국어 메뉴](docs/screenshots/korean-menu-r38.png) | 개발 중 확인한 한국어 명령 메뉴 예시(r38 캡처). |
| ![보이스 자막](docs/screenshots/voice-subtitle-r249.png) | r249 게임 + r44 전용 코어에서 음성 진행에 따라 나타난 한국어 자막. 초상화와 자막이 같은 하단 영역을 공유할 수 있습니다. |
| ![오프닝 인물과 자막](docs/screenshots/intro-portraits-r249.png) | r249/r44에서 캡처한 복수 초상화 장면의 한국어 자막 예시. |

스크린샷은 실제 개발·검증 실행의 정지 화면이며, 서로 다른 시점의 캡처를 함께 보여줍니다. 한 장의 그림만으로 모든 장면의 표시 품질이나 타이밍을 보증하지 않습니다.

## 받기 전에 확인할 것

1. [Releases](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/releases)에서 `v0.75`의 `SnatcherKRInstaller.exe` 또는 같은 EXE가 든 ZIP을 받습니다. **Windows 64비트용 패처**이며 APK 생성기나 RetroArch 수정 도구가 아닙니다.
2. 본인이 보유한 미국판 원본 `Snatcher (USA).bin`을 준비합니다. 파일 크기 **625,192,176바이트**, SHA-256 **`8d6f4dba8d9ce59991be9f65635047adc3b0f37ea2358f8c48b251883c9e55b6`**, CRC32 **`3faf807d`**만 입력으로 받습니다. 다른 덤프·다른 리전·이미 수정된 BIN은 거부합니다.
3. 결과를 넣을 **이미 존재하는 빈 폴더**를 준비합니다. 약 **700MB 이상**의 여유 공간이 필요합니다. 패처는 동명 파일을 덮어쓰지 않습니다.

## 패처 사용법

1. ZIP으로 받았다면 압축을 풀고 `SnatcherKRInstaller.exe`를 실행합니다. Windows 보안 경고가 뜨면 발행자와 [아래 SHA-256](#sha-256-검증)을 확인한 뒤 본인이 실행 여부를 판단하세요.
2. **원본 BIN 선택**에서 위의 `Snatcher (USA).bin`을 지정합니다. 패처가 크기·SHA-256·CRC32를 확인합니다.
3. **결과 폴더 선택**에서 빈 폴더를 지정하고 설치를 누릅니다. 패처가 BPS를 적용한 뒤 출력 BIN과 동봉 파일의 해시를 확인합니다. 실패하면 원본 BIN은 바뀌지 않습니다.
4. 결과 폴더에서 `Snatcher (USA) [KR Voice PC68 English r249].bin`과 같은 이름의 `.cue`를 **함께 보관**합니다. RetroArch에서 게임을 열 때는 **`.bin`이 아니라 `.cue`**를 선택하세요. 이렇게 해야 CD 오디오 트랙 참조를 유지할 수 있습니다.
5. 사용하는 플랫폼에 맞는 **전용 코어**를 설치·선택하고 게임 `.cue`를 엽니다. 일반 코어로 열면 한국어 보이스 자막 기능이 빠집니다. BIOS는 RetroArch 안내에 따라 사용자가 별도로 설정해야 합니다.

### 플랫폼별 코어

| 플랫폼 | 전용 코어 파일 | 상태 |
| --- | --- | --- |
| Windows x86_64 | `genesis_plus_gx_snatcher_kr_libretro.dll` | 패처가 함께 출력합니다. Windows 실행·출력 해시 검증을 수행했습니다. |
| Android ARM64 | `genesis_plus_gx_snatcher_kr_libretro_android.so` | 패처가 함께 출력합니다. APK는 수정하지 않습니다. 실제 Android 기기의 코어 로딩·게임 재생은 아직 미검증입니다. |
| Linux x86_64 | `genesis_plus_gx_snatcher_kr_libretro.so` | 패처가 함께 출력하고, 릴리스에서 단독으로도 받을 수 있습니다. Ubuntu 24.04 x86_64에서 빌드·ELF/의존성 검사를 통과했습니다. 게임 재생은 미검증입니다. |

Windows에서는 출력된 DLL을 RetroArch의 사용자 코어 위치에 복사하거나 코어 파일을 직접 불러옵니다. Android에서는 출력된 ARM64 SO를 기기로 옮긴 뒤 기기 RetroArch에서 외부 코어 설치/가져오기 기능을 사용합니다. Linux에서는 Linux x86_64 SO와 같은 이름의 `.info`를 코어 및 코어 정보 위치에 두거나 해당 SO를 직접 불러옵니다. 버전·배포 방식에 따라 메뉴 이름과 코어 경로가 다를 수 있으므로 설치된 RetroArch의 안내를 확인하세요. Android용 SO를 Linux용으로, Linux용 SO를 Android용으로 바꿔 쓸 수는 없습니다.

패처는 게임 BIN/CUE, Windows DLL, Android ARM64 SO, Linux x86_64 SO, 코어 정보 `.info`, 코어·폰트 라이선스, 개조 코어의 전체 소스 ZIP과 빌드 기록을 한 폴더에 출력합니다. 원본 BIN, 기존 파일, RetroArch 설치본은 덮어쓰지 않습니다.

### Windows 없이 수동 적용하기

Linux/Android만 사용하는 사람을 위해 릴리스에 `Snatcher-KR-r249-development-a.bps`, 결과 `.cue`, Linux 전용 `.so`도 개별 자산으로 제공합니다. BPS 지원 패처에서 **위 해시의 원본 BIN → BPS → 새 결과 BIN** 순서로 적용하세요. 결과 BIN 이름을 `Snatcher (USA) [KR Voice PC68 English r249].bin`으로 맞추고, 릴리스의 같은 이름 `.cue`와 같은 폴더에 두세요. 결과 SHA-256이 아래 값과 일치해야 합니다. 이 경로에서는 전용 코어도 별도로 받아야 하며, 원본·결과 게임 자체는 릴리스에 없습니다.

## SHA-256 검증

아래 값은 **v0.75에 사용하는 r249 게임·r44 코어**의 기준입니다. 해시가 맞지 않으면 임의로 실행하지 말고 파일·버전을 다시 확인하세요.

| 대상 | 크기(바이트) | SHA-256 | CRC32 |
| --- | ---: | --- | --- |
| 입력 원본 `Snatcher (USA).bin` | 625,192,176 | `8d6f4dba8d9ce59991be9f65635047adc3b0f37ea2358f8c48b251883c9e55b6` | `3faf807d` |
| 출력 한국어 r249 BIN | 625,192,176 | `132465a0f16f40f6d21eda440ba059a6b7da99cf74bb72af35d4afa898404737` | `04e7b83b` |
| 내장 BPS 패치 | 1,113,399 | `622e3c77e5b0f43db8556df4bcf9312293e2e18dbcf52b2e96eb30bdb7a0f028` | `2144df1c` |
| 출력 Windows r44 DLL | 5,814,955 | `e4ff3f4ee31f8114ba5adf72e7c19f8a02f1b8b1ce5fb8a6670ae2541f97b95e` | `a044b6cc` |
| 출력 Android ARM64 r44 SO | 8,653,616 | `c51ff189cf4e76d5345736720c3e90ee449806a6afe35dffe33a7e0b1556b7af` | `5e257191` |
| 출력 Linux x86_64 r44 SO | 8,710,104 | `114f709a38fff20a7f07a6655fb712aef2190746faed8a1cc43477424e65b879` | — |
| 결과 CUE | 1,389 | `331dd60c3567c67a72398f5d725b78d05754024ca958838e68b90e2f2e9c6637` | `219f44c8` |
| v0.75 패처 EXE | 34,565,054 | `755bb0f8340a8d219f5513e510f8bdbea2df7ba7f6d00cfd6559d6d786d2a8bc` | — |

Windows PowerShell에서 수동 확인: `Get-FileHash -Algorithm SHA256 -LiteralPath '파일경로'`. Linux에서는 `sha256sum '파일경로'`를 사용할 수 있습니다. 파일명보다 **해시**를 우선하여 판별하세요. 릴리스 ZIP의 해시는 해당 [v0.75 릴리스](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/releases/tag/v0.75)에 별도로 적습니다.

## 확인 범위와 알려진 제한

- Windows 패처의 페이로드 검사·UI 기동을 확인했고, Linux 코어 추가형 패처의 전체 크기 원본 BIN 적용 시험에서는 결과 파일 11개가 기대 해시와 일치했습니다. 설치 로직 자동 시험 7/7 통과했습니다. 최종 v0.75 EXE는 세 코어의 페이로드 검사·UI 기동을 통과했습니다.
- r249/r44의 화면·음성 자막은 일부 장면에서 확인했지만, 모든 대사와 전편을 사람 눈·귀로 최종 승인한 것은 아닙니다. 장면에 따라 자막이 초상화 위에 겹칠 수 있습니다.
- Android 기기 실사용, 실기 Mega CD, Linux 코어의 실제 게임 재생은 별도 검증이 필요합니다. 해당 결과가 나오기 전까지 검증 완료로 표기하지 않습니다.
- 문제가 발생하면 게임 화면, 사용 플랫폼·코어 파일 해시, 원본 BIN SHA-256, 해당 장면과 재현 순서를 함께 남겨 주세요. 원본 게임/BIOS 파일은 첨부하지 마세요.

## 소스와 고지

전용 코어의 [완전한 개조 소스](core-source/modified-core-source.zip)와 [코어 라이선스](licenses/CORE-LICENSE.txt), [Galmuri 글꼴 라이선스](licenses/Galmuri-OFL-1.1.txt)를 제공합니다. 코어 소스에 관한 조건과 게임 원작의 권리는 서로 다릅니다. 이 저장소는 원작 게임에 대한 권리를 주장하지 않습니다. 게임·BIOS는 배포하지 않으며, 사용자 소유 원본에 적용하는 패치만 제공합니다.
