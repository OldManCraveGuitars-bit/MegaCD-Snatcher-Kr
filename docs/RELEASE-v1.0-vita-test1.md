# V1.0 PS Vita 전용 코어 시험판

**비타 RetroArch용 `.self` 빌드입니다. 컴파일 및 정적 검사를 통과했으며, 비타 실기 실행·속도·음성·자막 재생은 아직 확인하지 않았습니다.** 정식 V1.0 게임 패치 내용과 기존 3개 플랫폼 코어는 변경하지 않습니다.

## 받는 파일

- **`Snatcher-KR-V1.0-Vita-test1.zip`**: 설치용 전용 SELF, 코어 정보, 한국어 설치 안내, 빌드 명세, 라이선스.
- `genesis_plus_gx_snatcher_kr_libretro.self`: 실행 파일만 필요한 경우.
- `Snatcher-KR-V1.0-Vita-source.tar.xz`: 해당 RetroArch 전체 소스, r61 개조 코어 소스, 프런트엔드 수정 패치 및 빌드 스크립트.
- `BUILD-VITA.json`: 사용한 소스/컴파일 환경/파일 해시와 검사 결과.
- `SHA256SUMS-Vita-test1.txt`: 배포 파일 SHA-256 목록.

**게임과 BIOS는 포함하지 않습니다.** 기존 [V1.0 패처](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/releases/tag/v1.0)로 만든 BIN/CUE를 사용하세요. 기존 Windows 패처에는 Vita 파일이 없으며 이 릴리스의 ZIP을 별도로 받아야 합니다.

## 간단한 실행 순서

1. 일반 Vita RetroArch 1.22.2가 설치된 환경에서 RetroArch를 종료합니다.
2. ZIP의 전용 `.self`를 `ux0:/app/RETROARCH/`에, 같은 이름의 `.info`를 `ux0:/app/RETROARCH/info/`에 추가합니다. 코어 정보 경로를 변경한 환경은 설정된 위치를 사용합니다.
3. 설정된 시스템/BIOS 폴더에 본인 소유 `bios_CD_U.bin`을 준비합니다.
4. 패치한 `Snatcher-KR-v1.0.bin`과 `.cue`를 같은 폴더에 복사합니다.
5. 전용 코어 **Snatcher KR V1.0 Vita test1**을 선택하고 **CUE**를 엽니다.

기존 `genesis_plus_gx_libretro.self`나 `eboot.bin`을 덮어쓰지 않습니다. **DLL/SO를 SELF로 이름만 바꿔서는 사용할 수 없습니다.**

[자세한 비타 설치 방법과 확인 범위](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/main/docs/PS-VITA.md)

## 빌드 내용과 검사

- V1.0 r61 코어 + RetroArch v1.22.2, VitaSDK 2026.08/GCC 15.2.0.
- Vita2D 메뉴 행렬 인수의 타입 오류 한 줄 교정. 변경 패치와 적용 후 전체 소스 동봉.
- 코어와 프런트엔드의 CRC 함수가 충돌하지 않도록 코어 빌드에서 함수명을 구분. 기존 계산 코드 유지, 두 구현의 별도 연결 검사.
- ARM 32비트 ELF, 코어/자막 필수 함수 6개, SELF 컨테이너 생성 확인.
- V1.0 자막 비트맵 은행 **33/33개**의 최종 ELF 바이트 일치, 추가 CD 음성 자막 **431쪽** 내장 확인.
- 음성 중심 시각·흰 글씨·검은 테두리·하단 표시를 구현한 기존 코어 소스와 번역 데이터는 유지했습니다. 이 항목은 소스/데이터 보존 확인이며 비타 화면에서의 실측 결과가 아닙니다.
- 실제 비타 부팅·메뉴 로딩·게임 재생·성능·저장 호환성은 미검증입니다. Piglet 배포판을 대상으로 빌드하지 않았습니다.

[성공한 빌드 및 검사 기록](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/actions/runs/40302827118)

SELF: **4,574,527바이트**, SHA-256 `13a339f9acc4d45ca3d2f8477d98f52a5fbcd68db384c1e52f0b401b6837cac3`

설치 ZIP SHA-256: `7b01406e68c2a84aee1a9a908bc3f983e767e238ebb5a2718aabe2c446ad000a`

[전체 배포 파일 해시](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/main/SHA256SUMS-Vita-test1.txt)

원본 BIN SHA-256: `8d6f4dba8d9ce59991be9f65635047adc3b0f37ea2358f8c48b251883c9e55b6`

V1.0 결과 BIN SHA-256: `96b1032147780f24748b54f85fc1210fecfe8beadb860b416764c64bfe493646`

이 릴리스는 별도 시험판이며 최신 정식 릴리스는 **비공식 한글화 정식버전 V1.0**으로 유지됩니다.
