# V1.02 PS Vita 전용 코어 시험판 — r62

**ACT1→ACT2 연속 진행 보이스 자막 누락을 수정한 Vita r62 SELF입니다. 빌드·정적 검사는 통과했지만 실제 비타 부팅·음성·자막·속도는 아직 확인하지 않았습니다.**

**V1.01 게임 BIN/CUE는 그대로 두고 전용 SELF와 INFO만 교체하세요.** V1.0 이하 게임은 [V1.02 패처](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/releases/tag/v1.02)로 미국판 원본에서 패치해야 V1.01의 전환 정지 수정도 적용됩니다. 게임/BIOS/VPK는 포함하지 않습니다.

## 받는 파일

- **`Snatcher-KR-V1.02-Vita-test1.zip`**: 설치용 전용 SELF/INFO, 한국어 설치 안내, 빌드 명세와 라이선스.
- `genesis_plus_gx_snatcher_kr_libretro.self`: 실행 파일만 필요한 경우.
- `Snatcher-KR-V1.02-Vita-source.tar.xz`: 해당 RetroArch 전체 소스, r62 코어 소스, 프런트엔드 수정 및 빌드 도구.
- `BUILD-VITA.json`: 빌드 입력·환경·자막 은행·수정 overlay 해시와 검증 한계.
- `SHA256SUMS-Vita-v1.02-test1.txt`: 전체 배포 파일 해시.

## 설치

1. 일반 Vita RetroArch 1.22.2를 완전히 종료하고 저장을 백업합니다. Piglet용 빌드는 아닙니다.
2. ZIP의 전용 SELF를 `ux0:/app/RETROARCH/`에, 같은 이름의 INFO를 `ux0:/app/RETROARCH/info/`에 넣습니다. INFO 경로를 변경했다면 설정된 위치를 사용합니다. 이전 전용 시험판의 두 파일은 교체하고 일반 코어와 `eboot.bin`은 유지합니다.
3. 시스템/BIOS 폴더에 본인 소유 `bios_CD_U.bin`을 준비합니다.
4. **Snatcher KR V1.02 Vita test1** 코어를 선택하고 V1.01 또는 V1.02 **CUE**를 엽니다. BIN/CUE는 같은 폴더에 두고 파일명을 맞춥니다.
5. 게임 내 저장을 불러옵니다. 옛 세이브스테이트의 호환성을 보증하지는 않습니다.

[자세한 설치 방법](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/v1.02-vita-test1/docs/PS-VITA.md)

## 확인 범위

- Windows·Android·Linux와 동일한 r62 코어 소스를 ARM용으로 컴파일하고 RetroArch1.22.2와 정적 링크했습니다. ACT2 자막의 실제 표시 구간에서 지난 PCM 상태를 해제하는 수정입니다. DLL/SO의 확장자를 바꾼 파일이 아닙니다.
- ARM32 ELF·필수 함수6개·SELF 컨테이너 및 자막 은행33/33개 바이트 일치 확인. 기존 추가 CD 자막431쪽·문구·시간표·흰 글씨/검은 테두리 데이터는 유지합니다.
- r62 overlay SHA와 전체 코어 입력 ZIP을 고정해 빌드했습니다. SDK·프런트엔드 수정은 이전 시험판과 동일하며 해당 소스/패치/라이선스를 동봉합니다.
- [성공한 빌드 기록](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/actions/runs/43738776565). **비타 실기·에뮬레이터 실행, 프레임 속도, 저장 호환성은 미검증**입니다. PC 화면을 비타 실행 증거로 제시하지 않습니다.

SELF: **4,574,405바이트**, SHA-256 `15180ca012d9e9381f6e617c7554435b7dda73ae59df19097cc12af804c2e251`

설치 ZIP SHA-256: `12d0778ca3f0608d0c53944d52072833f7b87c6b0f2e9c820ad7ddaed62b186f`

코어 입력 ZIP SHA-256: `58b49adcbb6bfe9bd3595e42866968053ccd7f9755d31bbae1588fc722c95741`

수정 overlay SHA-256: `30d8dd841a9b7f815a6c2188cd964f961433d5e6fb947c242c1c4bf8ccdb7f2e`

게임 V1.01/V1.02 BIN SHA-256: `dd91fc991ab5e7feb0c965cc15e001d9c0ff6dc24e7b504293b51dec6447381f`

[전체 Vita 배포 해시](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/v1.02-vita-test1/SHA256SUMS-Vita-v1.02-test1.txt) · [V1.02 수정·검증 상세](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/v1.02/docs/RELEASE-v1.02.md)

별도 시험판으로 제공하며 최신 정식 릴리스는 **비공식 한글화 정식버전 V1.02**입니다.
