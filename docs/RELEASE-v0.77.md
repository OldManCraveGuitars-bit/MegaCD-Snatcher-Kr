# v0.77 — CD 음성 누락 자막 복원·전용 코어3종

**음성을 따라가는 한국어 보이스 자막 패치입니다. 이번에 배포하는 전용 Genesis Plus GX 코어로 교체해야 추가 자막이 나옵니다.** Windows x86_64 DLL, Android ARM64 SO, Linux x86_64 SO를 제공합니다. RetroArch 본체와 APK는 수정하지 않습니다.

## 복원한 내용

처음 폐허로 이동할 때 길리언의 독백4문장이 빠져 있었습니다. 해당 음성은 기존 PCM 목록 밖의 **CD 오디오 Track20**에 있었고, v0.76 코어에 연결되지 않았습니다. 이를 복원하면서 다른 미등록 CD 음성도 조사해 **13개 트랙·자막426쪽**을 추가했습니다. 426은 표시 페이지 수이며 독립 문장 수가 아닙니다.

아래 표에는 후반 장면의 이름이 포함됩니다.

| CD 트랙 | 표시쪽 | 추가 자막 구간 |
| --- | ---: | --- |
| 06 | 19 | 첫 사건 뒤 정커 본부 귀환·국장 보고 |
| 07 | 44 | 랜덤 등장 및 병원에 관한 대화 |
| 10 | 36 | 병원 관련 통화 |
| 11 | 35 | 차량 추격·구출·거리 경고 |
| 12 | 65 | 해리의 마지막 대화 |
| 13 | 24 | 국장 전투 이후 대화 |
| 14 | 16 | 제이미 관련 통화·협박 |
| 15 | 35 | 미카와의 작별·메탈의 재촉 |
| 17 | 20 | 탑승 방송·마지막 작별 |
| 18 | 9 | 정커의 앞으로의 활동에 관한 대화 |
| 19 | 20 | 메탈의 마지막 대화 |
| 20 | 4 | 처음 폐허로 향하는 길리언의 독백 |
| 21 | 99 | 병원 지하에서의 대치와 탈출 대화 |
| 합계 | 426 | 13트랙 |

추격 중150/70미터 경고, 미카 대화 사이 메탈의 재촉, 탑승 방송3문장 등 전사에서 빠지기 쉬운 발화도 보완했습니다. 긴 문장은 의미를 버리지 않고 음성의 절에 맞춰 페이지로 나눴습니다. 기존 엔딩의5줄 인용 문구는 화면 번역을 유지하고 중복 하단 자막을 만들지 않았습니다.

이전 v0.76의 “고유 음성1,119개 전체 검수”는 **등록된 PCM 자막 목록의 내용 검수**였으며, 별도 CD 트랙의 모든 누락을 확인했다는 뜻은 아니었습니다. 이번에 발견한 누락은 그 범위 밖에 있었습니다. 원음의 기계 전사·단어 시각과 문맥을 대조했으며 일부 구간을 더 큰 모델로 확인했지만, 사람의 전편 청취 승인이나 모든 누락이 없다는 보증은 아닙니다.

## 유지되는 것

- v0.76의 본문·선택문, 말투·문맥 교정, PCM 자막, 제이미와 헤어질 때의 “잘 안 들려!” 복원은 그대로입니다.
- 승인된 오프닝 내레이션 및 기존 Track03/04/08/09 시각을 바꾸지 않았습니다.
- 화면 넘김이 아니라 **CD 음성 재생 시계**를 사용합니다. 기존 최종 픽셀 합성 방식으로 하단에 흰 글자와 밀착 검은 테두리만 그립니다. 자막 바깥 영역은 투명하며 게임RAM/VRAM/CRAM/SAT에 쓰지 않습니다.
- **게임 BIN/BPS는 v0.76 r251과 동일**합니다. 달라진 것은 r47 전용 코어와 패키지 이름입니다.

## 설치·업데이트

### v0.76을 사용 중이라면

아래 한국어 BIN 해시와 일치하면 **게임을 다시 패치할 필요 없이 v0.77 전용 코어만 교체**해도 됩니다. 실행 중인 게임을 종료하고, 플랫폼에 맞는 새 코어로 기존 BIN/CUE를 여세요. 기존 BIN/CUE 이름은 그대로 써도 됩니다. v0.77 CUE만 따로 받아 기존 이름의 BIN과 섞지 마세요. CUE 안의 파일명과 실제 BIN 이름이 일치해야 합니다.

기존 세이브스테이트 호환성은 보증하지 않습니다. 가능한 게임 내 저장으로 이어 하세요. 일반 코어 또는 이전 전용 코어에서는 이번 추가 CD 음성 자막이 나오지 않습니다.

### 신규 설치 또는 v0.75에서 업데이트

1. `MegaCD-Snatcher-Kr-v0.77-Windows-Patcher.zip`을 풀고 `SnatcherKRInstaller.exe`를 실행합니다. EXE 단독 자산도 같은 프로그램입니다.
2. 아래 해시와 일치하는 미국판 **원본 BIN**을 선택합니다. 이미 패치한 BIN에 덧씌우는 방식이 아닙니다.
3. 이미 존재하는 빈 출력 폴더를 선택합니다. 약700MB 이상의 공간을 준비하세요. 패처는 입력 원본과 기존 동명 파일을 덮어쓰지 않습니다.
4. 패처가 한국어 BIN/CUE, Windows·Android·Linux 전용 코어3종, 코어정보, 라이선스, 개조 코어 전체소스와 빌드 기록을 출력하고 해시를 검사합니다.
5. `Snatcher-KR-v0.77.bin`과 `Snatcher-KR-v0.77.cue`를 함께 두고, RetroArch에서 플랫폼에 맞는 전용 코어로 **`.cue`**를 엽니다. BIOS는 사용자가 별도로 준비합니다.

| 플랫폼 | 설치할 전용 코어 |
| --- | --- |
| Windows x86_64 | `genesis_plus_gx_snatcher_kr_libretro.dll` |
| Android ARM64 | `genesis_plus_gx_snatcher_kr_libretro_android.so` |
| Linux x86_64 | `genesis_plus_gx_snatcher_kr_libretro.so` |

Android APK를 만들거나 바꾸지 않습니다. Android와 Linux는 둘 다 `.so`지만 서로 다른 파일이며 바꿔 쓸 수 없습니다. Windows 없이 설치하려면 개별 `Snatcher-KR-v0.77.bps`를 BPS 지원 도구로 원본에 적용하고, 결과 이름을 `Snatcher-KR-v0.77.bin`으로 맞춘 뒤 동봉 CUE와 해당 플랫폼 코어를 사용하세요.

[상세 설치 안내](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/v0.77/README.md)에 플랫폼별 설명이 있습니다. 원본 게임, 패치 완료 게임, BIOS, RetroArch APK는 배포하지 않습니다.

## 패치 전후 식별값

| 대상 | 크기(바이트) | SHA-256 | CRC32 |
| --- | ---: | --- | --- |
| 입력 미국판 BIN | 625,192,176 | `8d6f4dba8d9ce59991be9f65635047adc3b0f37ea2358f8c48b251883c9e55b6` | `3faf807d` |
| 출력 한국어 BIN(v0.76과 동일) | 625,192,176 | `8cc04b83d18b5c6eb897523b89ed17f627314c8457732c6f77d3328c1d9fec3a` | `d211942f` |
| 패처 EXE | 34,778,165 | `fe6e0f70bb5885a12a7af7e891b4ae19201d5ee78bc4511b0a8a4badba76c64e` | `1421d770` |
| Windows DLL | 6,229,352 | `e25e8c89a32be485be20c51ce93e7aca510225c55322a9d68bce6511cdf25f05` | `1dc529a7` |
| Android ARM64 SO | 9,067,776 | `47955aed3d23409a36f2d92204cafca8f32466ac0866df744a21bf2f6a944efa` | `32620633` |
| Linux x86_64 SO | 9,124,016 | `d571fe6d6f7d2b22bb5e4e70eb0650447865b8d009cfb6ab0e9865c1c92555c3` | `7cc5f510` |

전체 파일과 ZIP의 해시는 [SHA256SUMS-v0.77.txt](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/v0.77/SHA256SUMS-v0.77.txt)에 있습니다. PowerShell `Get-FileHash -Algorithm SHA256`, Linux `sha256sum`으로 확인할 수 있습니다.

## 확인 범위와 제한

- 최종426쪽을 실제 C 소비처에서 검사:13트랙151,169섹터, 모든 페이지의 흰/검정/투명 픽셀, 두 픽셀 바이트순서,9비활성 조건과 게임RAM 불변. 관련 자동시험19통과. 이것은 전편 플레이나 사람이 음성을 듣고 승인한 결과가 아닙니다.
- 배포하는 **실제 EXE**로 원본625,192,176바이트 게임을 패치해 출력11/11파일의 크기/SHA-256/CRC32 일치 및 원본 불변을 확인했습니다.
- 원본ISO99파일에서 미등록PCM16자산의 재생명령 참조를 찾지 못해 임의로 연결하지 않았습니다. 효과음 후보27개 재분류에서 추가 의미 있는 누락 대사는 확인하지 못했습니다. 정적 검색 결과만으로 절대적인 미사용을 증명하지는 않습니다.
- Windows r251/r47 새게임으로 만든 동일 제품 체크포인트에서 정상 메뉴 경로로 첫 폐허까지 진행해 독백4/4문장의 실제 표시를 확인했습니다. 장면/RAM 주입 없이 진행했고 입력 게임·코어 파일은 바뀌지 않았습니다. 녹화 음성과 원음의4지점 상관값0.929~0.961, 독백 구간 재생 비율1.0으로 정렬했으며 자막 전후 비표시도 확인했습니다. 같은 실행의 원본 해상도 캡처4/4에서 기대 흰 글자·검은 테두리의 색 불일치0을 확인했습니다. 새로운 CD 자막 전 구간을 다시 플레이한 것은 아닙니다.
- Linux Ubuntu24.04 x86_64 소스 해시·빌드·ELF/의존성·동적로드/libretro API1 검사는 [Actions 기록](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/actions/runs/38457704182)에 있습니다. Android/Linux 실제 게임 재생과 실기 Mega CD는 미검증이며, 실기용 ROM만의 패치가 아닙니다.

## 새 독백 실제 표시 — v0.77 r251/r47

네 장 모두 위 정상 경로 실행에서 캡처했습니다. 원본 해상도 프레임을 최근접 확대했으며, 글자를 사후에 얹은 설명용 합성이 아닙니다. 자막 네 문장은 CD 음성 재생에 따라 바뀝니다. 도착 이전 본부 준비 구간의 빠른 진행은 종료한 뒤 독백을 정상 속도로 확인했습니다. 이 네 장은 다른12트랙이나 전편 플레이의 증거가 아닙니다.

![첫 폐허 독백1 출근 첫날](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/v0.77/docs/screenshots/factory-r251-r47-card01.png)

![첫 폐허 독백2 깁슨의 추적](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/v0.77/docs/screenshots/factory-r251-r47-card02.png)

![첫 폐허 독백3 스내처일까](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/v0.77/docs/screenshots/factory-r251-r47-card03.png)

![첫 폐허 독백4 훈련의 성과](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/v0.77/docs/screenshots/factory-r251-r47-card04.png)

## 기존 화면 예시

아래는 기존 r249/r45의 정상속도 녹화에서 추출한 오프닝2 복원 화면입니다. 해당 자막 데이터와 시각은 v0.77에서도 유지되며, 이번 추가13트랙의 실행 증거로 제시하는 사진은 아닙니다.

![제이미와 헤어질 때 복원한 잘 안 들려 자막](https://raw.githubusercontent.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/v0.77/docs/screenshots/farewell-r249-r45-card03.png)

[오프닝 갤러리12장](https://github.com/OldManCraveGuitars-bit/MegaCD-Snatcher-Kr/blob/v0.77/docs/OPENING-GALLERY.md)에서 각 사진의 빌드 출처와 함께 더 많은 화면을 볼 수 있습니다.

완전한 개조 코어 소스980파일은 `modified-core-source.zip`, 입력 식별값과 재현 명령은 `CORE-BUILD.json`/`CORE-REPRODUCTION.json`으로 제공합니다. 컴파일러/플랫폼에 따른 비트 단위 동일 재빌드를 보증하지 않습니다. 원본 코어와 Galmuri 글꼴의 라이선스 고지를 함께 제공합니다.
