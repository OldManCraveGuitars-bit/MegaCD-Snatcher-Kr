# v0.75 — 보이스 자막 통합 패처·전용 코어 3종

미국판 Mega CD *Snatcher*에 한국어 게임 문구·선택문과 **음성 연동 한국어 자막**을 적용하는 시험판입니다. 자막은 게임의 화면/문장 넘김과 분리된 전용 코어에서 그립니다. **일반 Genesis Plus GX 코어에서는 이 보이스 자막이 나오지 않습니다.** Windows DLL, Android ARM64 SO, Linux x86_64 SO 가운데 플랫폼에 맞는 전용 코어를 사용해야 합니다.

## 무엇을 받나

- Windows 사용: `MegaCD-Snatcher-Kr-v0.75-Windows-Patcher.zip`을 풀고 `SnatcherKRInstaller.exe`를 실행하세요. EXE 단독 다운로드도 같은 프로그램입니다. 원본 BIN을 검사하고 한국어 BIN/CUE와 전용 코어 3종을 한꺼번에 출력합니다.
- Linux/Android에서 수동 패치: `Snatcher-KR-r249-development-a.bps`, 결과용 `Snatcher-KR-r249.cue`, 해당 플랫폼 `.so`와 공용 `.info`를 받으세요. CUE 안의 `FILE` 지시문이 가리키는 이름으로 결과 BIN을 저장하세요. BPS 지원 도구로 본인이 보유한 정확한 미국판 BIN에 적용해야 합니다. Android APK는 수정하거나 배포하지 않습니다.
- 코어의 완전한 개조 소스는 `modified-core-source.zip`, 고지는 `CORE-LICENSE.txt`와 `Galmuri-OFL-1.1.txt`에 있습니다. 게임 원본·결과 BIN, BIOS는 배포하지 않습니다.

자세한 [단계별 패처 사용법·플랫폼 설치·주의사항](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/main/README.md)을 먼저 읽어 주세요.

## 원본과 결과 해시

| 파일 | 크기 | SHA-256 |
| --- | ---: | --- |
| 입력 `Snatcher (USA).bin` | 625,192,176바이트 | `8d6f4dba8d9ce59991be9f65635047adc3b0f37ea2358f8c48b251883c9e55b6` |
| 출력 `Snatcher (USA) [KR Voice PC68 English r249].bin` | 625,192,176바이트 | `132465a0f16f40f6d21eda440ba059a6b7da99cf74bb72af35d4afa898404737` |

원본과 결과 CRC32는 각각 `3faf807d`, `04e7b83b`입니다. EXE, BPS, CUE, 세 코어, 소스 ZIP의 SHA-256은 [체크섬 목록](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/main/SHA256SUMS-v0.75.txt)에 모두 기록했습니다. 패치 뒤에는 **결과 `.cue`**를 열어 CD 오디오 트랙을 유지하세요.

## 화면 예시

![r249 타이틀](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/main/docs/screenshots/title-r249.png)

r249의 타이틀. 원본 연출을 유지합니다.

![한국어 명령 메뉴](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/main/docs/screenshots/korean-menu-r38.png)

한국어 명령 메뉴의 개발 중 캡처(r38). 게임 내 문구와 선택문 번역의 예시입니다.

![음성 자막과 초상화](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/main/docs/screenshots/voice-subtitle-r249.png)

r249 게임 + r44 전용 코어에서 음성에 따라 나타난 하단 자막. 초상화와 같은 영역을 공유할 수 있습니다.

![복수 초상화](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/main/docs/screenshots/intro-portraits-r249.png)

복수 초상화 장면의 자막 예시. 스크린샷은 서로 다른 검증 시점의 정지 화면이며 전체 게임 동작 보증은 아닙니다.

### 오프닝 사진 12장 추가

초반 한국어 문구, 녹색 헌정 문구, 내레이션과 후반 기계 연출을 [오프닝 갤러리](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/main/docs/OPENING-GALLERY.md)에 모았습니다. 다음은 일부 미리보기입니다. 이 12장은 v0.75 직전 r248/r43의 실제 녹화에서 추출했으며, v0.75의 모든 픽셀이나 음성 동기화가 같다는 뜻은 아닙니다.

![오프닝 초반 문구](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/main/docs/screenshots/opening-r248-t010.png)

![녹색 헌정 문구](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/main/docs/screenshots/opening-r248-t030.png)

![오프닝 복도와 한국어 자막](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/main/docs/screenshots/opening-r248-t052.png)

![기계 손 연출](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/main/docs/screenshots/opening-r248-t108.png)

## 검증 수준

- 패처 자동 시험 7/7, 패키징 EXE의 페이로드 검사와 UI 기동 통과. Linux 코어 추가형의 625MB 실원본 적용 1/1, 결과 11/11 파일·잔여 부분 파일 0. 최종 EXE는 Linux 코어 출력 이름만 정리해 다시 패키징했고, 페이로드/UI 검사를 통과했습니다.
- Linux x86_64 코어는 Ubuntu 24.04에서 빌드되어 ELF·의존성·동적 로드와 libretro API v1 응답을 확인했습니다. 실제 Linux 게임 플레이는 아직 미검증입니다.
- Android 실기 로드·게임 재생, 전편 진행, 전 대사와 타이밍의 사람 검수는 완료 주장하지 않습니다. **시험판 v0.75**로 배포합니다.

비공식·비상업적 팬 패치입니다. 원작 게임·BIOS의 배포물이 아닙니다.
