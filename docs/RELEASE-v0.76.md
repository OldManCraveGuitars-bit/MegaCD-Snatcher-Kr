# v0.76 — 전체 대사 교정·오프닝2 누락 복원

**음성 진행을 따르는 한국어 보이스 자막 패치입니다. 함께 배포하는 전용 Genesis Plus GX 코어가 반드시 필요합니다.** Windows DLL, Android ARM64 SO, Linux x86_64 SO를 제공합니다. RetroArch 자체나 APK를 수정하지 않습니다.

## 이번 수정

- 본문·선택문10,728개, 고유 음성1,119개, 별도 오프닝/회상/정적 문구110개를 원문과 문맥에 맞춰 전부 대조했습니다. 말투뿐 아니라 의미 누락·주어/대상 역전·호칭·용어·중복 분기의 불일치를 검토했습니다.
- 본문1,491개, 고유 음성 번역175개, 음성 전사5개, 오프닝2 기존 문장2개, Act2 회상8개를 교정했습니다. 본문과 음성의 동일 대사는 중복될 수 있으므로 수치를 독립 대사 총수로 합산하지 않습니다.
- 미카와 메탈의 일반 대화는 존대, 국장이 길리언에게 말할 때는 반말/하게체, 해리는 연장자의 말투를 기준으로 맞췄습니다. 길리언은 상대에 따라 구분합니다. 인용·속마음·화난 발언까지 기계적으로 한 어미로 바꾸지는 않았습니다.
- 오프닝2에서 제이미와 헤어지는 구간의 **“제이미!” / “뭐라고?” / “잘 안 들려!”** 3장을 복원했습니다. 기존 오프닝 내레이션 및 음성 자막 페이지 시각은 유지했습니다.

## 받기·업데이트

Windows에서는 `MegaCD-Snatcher-Kr-v0.76-Windows-Patcher.zip`을 풀고 `SnatcherKRInstaller.exe`를 실행하세요. EXE 단독 파일도 같은 프로그램입니다. 정확한 미국판 원본 BIN과 이미 존재하는 빈 출력 폴더를 선택하면 한국어 BIN/CUE, 전용 코어3종, 코어 정보, 라이선스, 전체 개조 코어 소스와 빌드 기록을 함께 출력합니다.

**v0.75에 덧씌우지 말고 원본 BIN에서 다시 패치하세요. 게임과 코어를 모두 교체해야 교정된 보이스 자막이 나옵니다.** 기존 세이브스테이트 호환성은 보증하지 않습니다. 결과 `Snatcher-KR-v0.76.bin`과 `.cue`를 함께 두고, RetroArch에서는 **`.cue`**를 여세요.

Windows 없이 적용한다면 `Snatcher-KR-v0.76.bps`, `Snatcher-KR-v0.76.cue`, 해당 플랫폼 코어와 `.info`를 따로 받으세요. BPS 지원 도구로 아래 원본 BIN에 적용하고, 결과 이름을 `Snatcher-KR-v0.76.bin`으로 맞춥니다. Android SO와 Linux SO는 서로 대체할 수 없습니다.

[자세한 설치법과 플랫폼별 안내](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/v0.76/README.md)를 확인하세요. 게임 원본/결과 BIN, BIOS, APK는 배포하지 않습니다.

## 패치 전후 식별값

| 대상 | 크기 | SHA-256 | CRC32 |
| --- | ---: | --- | --- |
| 입력 미국판 BIN | 625,192,176 | `8d6f4dba8d9ce59991be9f65635047adc3b0f37ea2358f8c48b251883c9e55b6` | `3faf807d` |
| 출력 v0.76 BIN | 625,192,176 | `8cc04b83d18b5c6eb897523b89ed17f627314c8457732c6f77d3328c1d9fec3a` | `d211942f` |
| 최종 패처 EXE | 34,610,737 | `fb9a44e099977fd644d553d78346f40af42e70f602412adfadc8ca3de5f02eef` | `97e8f86a` |

모든 개별 배포 파일과 ZIP 해시는 [SHA256SUMS-v0.76.txt](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/v0.76/SHA256SUMS-v0.76.txt)에 있습니다. Windows PowerShell의 `Get-FileHash -Algorithm SHA256`, Linux의 `sha256sum`으로 확인할 수 있습니다.

## 누락 복원 화면

다음은 **r249 게임+r45 시험 코어의 정상속도 녹화**에서 추출한 실제 프레임입니다. 이3장의 자막 데이터와 시각은 최종 r46에도 그대로 포함됩니다. 스크린샷 자체는 전편 동작/음성 동기화 보증이 아닙니다.

![제이미!](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/v0.76/docs/screenshots/farewell-r249-r45-card01.png)

![뭐라고?](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/v0.76/docs/screenshots/farewell-r249-r45-card02.png)

![잘 안 들려!](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/v0.76/docs/screenshots/farewell-r249-r45-card03.png)

더 많은 장면은 [오프닝 갤러리](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/v0.76/docs/OPENING-GALLERY.md)에 있습니다. 각 사진의 개발판 출처를 함께 표기했습니다.

## 확인한 것과 한계

- 최종 게임 내 본문10,728개·폰트38개가 교정 카탈로그와 일치. 전용 코어의29음성모듈 자산이 최종 게임과 일치.
- 기존 음성1,130등록/1,647쪽 및 회상75쪽의 시각 유지. 전체 섹터 감사에서 허용 범위 외 변경 없음, 음성 트랙 불변. BPS2회 생성 결과 동일 및 독립 적용 검사 통과.
- **실제 배포 EXE**로 원본625MB 게임을 설치하여 결과11개 파일의 크기/SHA-256/CRC32 일치 및 원본 불변을 확인. 변경 표적 자동시험73통과/4선택조건 건너뜀, 최종 r251/r46 Windows 새부팅 확인.
- 이별3장 표시 및 원음 시간정렬을 기존 정상속도 녹화에서 확인. 모든 문장을 사람이 청취 승인하거나 모든 게임 분기를 다시 플레이했다는 뜻은 아닙니다.
- Linux Ubuntu24.04 x86_64 [빌드](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/actions/runs/38273324130)·[동적로드/API1](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/actions/runs/38273694350) 확인. Android/Linux 실제 게임 플레이 및 실기 Mega CD는 미검증입니다. **전용 코어가 필요한 시험판**으로 배포합니다.

완전한 개조 코어 소스980파일은 `modified-core-source.zip`에, 빌드 입력 식별값과 재현 명령은 `CORE-BUILD.json`/`CORE-REPRODUCTION.json`에 있습니다. 컴파일러/플랫폼에 따른 차이가 있으므로 비트 단위 동일 재빌드를 보증하지 않습니다. 원본 프로젝트의 라이선스와 Galmuri 폰트 고지를 함께 제공합니다.
