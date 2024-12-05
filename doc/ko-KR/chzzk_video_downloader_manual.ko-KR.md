# Chzzk Video Downloader
치지직 다시 보기 비디오 다운로드 도구

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_chzzkvideodownloader.png' />
<p><i>(이 이미지는 최신 정보와 다를 수 있습니다.)</i></p>
</div>

## 버전
Version 1.2.0, December 07, 2024 00:00:00

## 사용법
```powershell
ChzzkVideoDownloader [-h] [--version] [-i INPUT] [-a] [--authaut AUTHAUT] [--authses AUTHSES]
                     [--adult [ADULT]] [-y] [-q [QUALITY]] [-d [DISPLAY]] [--name [NAME]]
                     [--work [WORK]] [--out [OUT]] [--temp [TEMP]] [--category [CATEGORY]]
                     [--exist [EXIST]] [--threshold [THRESHOLD]] [--rpcid [RPCID]]
                     [--rpcport [RPCPORT]] [--snapshot SNAPSHOT] [--download [DOWNLOAD]]
                     [--thumb [THUMB]] [--startup [STARTUP]] [--settings [SETTINGS]] [--reset]
                     [video]
```

### 위치 매개 변수
```
video                   다운로드할 비디오 번호 또는 URL
```

### 선택적 매개 변수
```
-h, --help              도움말 메시지를 표시합니다
--version               버전 정보를 표시합니다
-i, --input INPUT       다운로드 목록 파일을 설정합니다
-a, --auth              치지직 인증 자격 증명을 설정합니다
--authaut AUTHAUT       치지직 인증 자격 증명의 인증 키를 설정합니다
--authses AUTHSES       치지직 인증 자격 증명의 세션 키를 설정합니다
--adult [ADULT]         자격 증명이 유효하지 않을 때 성인 콘텐츠 처리 방법을 설정합니다 (ask|skip)
-y, --yes               모든 확인 값을 자동으로 '예'로 설정합니다
-q, --quality [QUALITY] 다운로드하려는 목표 화질을 설정합니다. (예: 1080p)
-d, --display [DISPLAY] 다운로드 상태 표시 모드를 설정합니다 (quiet|simple|fluent|all)
--name [NAME]           저장되는 파일 이름 형식을 설정합니다
--work [WORK]           작업 디렉토리를 설정합니다
--out [OUT]             저장 디렉토리를 설정합니다
--temp [TEMP]           임시 디렉토리를 설정합니다
--category [CATEGORY]   저장 시 분류 방법을 설정합니다 (none|streamer)
--exist [EXIST]         파일이 이미 존재할 때 파일 저장 방법을 설정합니다 (rename|skip|overwrite)
--threshold [THRESHOLD] 디스크 공간 부족 시 중지 임계값(%)을 설정합니다. (비활성화: -, 기본값: 10, 3-30)
--rpcid [RPCID]         JSON-RPC 서버 ID를 설정합니다 (기본값: 30)
--rpcport [RPCPORT]     JSON-RPC 서버 포트를 설정합니다 (기본값: 63000, 49152-65300)
--snapshot SNAPSHOT     상태 변경 시 스냅샷을 JSON 파일로 저장합니다
--download [DOWNLOAD]   다운로드 방법을 설정합니다 (default|atxc|alter)
--thumb [THUMB]         미리보기 이미지의 저장 여부를 설정합니다 (save|skip)
--startup [STARTUP]     시작 방법을 설정합니다 (normal|fast)
--settings [SETTINGS]   설정 저장 시 동작을 설정합니다 (default|skip|quit)
--reset                 모든 설정을 초기화합니다
```

## 사용 예시
```powershell
ChzzkVideoDownloader 1602969 --thumb --work work --out out --temp temp
```

## 다운로드할 비디오 설정
비디오 번호 또는 URL을 직접 설정하여 다시 보기 비디오를 다운로드할 수 있습니다.

예를 들어, 비디오 URL이 https://chzzk.naver.com/video/1602969인 경우, 해당 비디오의 번호는 **1602969**입니다. 이 비디오를 다운로드하려면 아래 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader 1602969
ChzzkVideoDownloader https://chzzk.naver.com/video/1602969
```

여러 비디오를 순차적으로 다운로드하려면 아래와 같이 목록 파일을 작성한 후, UTF-8로 인코딩된 텍스트 파일로 저장합니다. (예: `list.txt`)

```python
# 목록 예시
https://chzzk.naver.com/video/2676946
2555164
https://chzzk.naver.com/video/2631744
https://chzzk.naver.com/video/2620211
https://chzzk.naver.com/video/2590216
2453109
```

그런 다음, 아래 명령어를 사용하여 다운로드합니다.

```powershell
ChzzkVideoDownloader -i list.txt
ChzzkVideoDownloader --input list.txt
```

## 인증 자격 증명 초기화
성인 전용 비디오와 같이 NAVER 인증 자격 증명이 필요한 비디오를 다운로드하려면 다음 정보를 지정해야 합니다.

* 치지직 쿠키에서 얻은 NAVER ID 인증 키 (`NID_AUT`)
* 치지직 쿠키에서 얻은 NAVER ID 세션 키 (`NID_SES`)

다운로드 시 인증 자격 증명을 찾을 수 없을 경우, 인증 정보를 입력하라는 메시지가 활성화됩니다.

이 값을 입력하면 기본값으로 설정되며, 이후 실행 시 추가 입력 없이 사용됩니다. 치지직 인증 자격 증명 획득 방법에 대한 자세한 정보는 `how_to_get_chzzk_credential.ko-KR.pdf`를 참고하세요.

인증 자격 증명이 변경되었거나 다른 ID로 로그인하여 인증 정보를 초기화해야 할 경우, 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url -a
ChzzkVideoDownloader video_no 또는 url --auth
```

`-y` 또는 `--yes` 매개 변수를 사용하면 확인 없이 인증 입력 메시지가 자동으로 활성화됩니다.

```powershell
ChzzkVideoDownloader video_no 또는 url -y
ChzzkVideoDownloader video_no 또는 url --yes
```

## 다운로드할 목표 화질 지정
기본적으로 모든 비디오는 가능한 최상의 화질로 다운로드됩니다. 그러나 저장 공간을 절약하거나 다른 이유로 화질을 변경하여 저장하려면 다음 명령어를 사용하세요. 또한, 비디오가 표준 해상도를 사용하지 않는 경우에는 지정한 해상도와 가장 가까운 화질로 자동 선택됩니다.

```powershell
ChzzkVideoDownloader video_no 또는 url -q 720p
ChzzkVideoDownloader video_no 또는 url --quality 720p
```

이 옵션을 기본값으로 되돌리려면 형식 없이 `-q` 또는 `--quality`만 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url -q
ChzzkVideoDownloader video_no 또는 url --quality
```

## 저장 파일 이름 형식 설정
기본적으로 비디오와 미리보기 파일 이름은 `[{live_date}][{name}] {title}` 형식으로 저장됩니다. 이 형식을 변경하려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --name "[{name}][{category}] {title}"
```

이 선택 사항을 기본값으로 되돌리려면 형식 없이 `--name`만 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --name
```

### 파일 이름 형식 태그
다음과 같은 미리 정의된 태그를 파일 이름 형식에 사용할 수 있습니다.

* `{name}` - 채널 이름.
* `{verified}` - 채널이 인증된 경우 `[✓]`이며, 그렇지 않은 경우 빈 값입니다.
* `{video_no}` - 비디오 번호.
* `{title}` - 비디오 제목.
* `{category_type}` - (설정되어 있을 경우) 비디오의 카테고리 형식.
* `{category}` - (설정되어 있을 경우) 비디오의 카테고리.
* `{category_value}` - (설정되어 있을 경우) 비디오의 카테고리 값.
* `{live_date...}` - 스트리밍 시작 시점의 날짜 관련 태그.
* `{publish_date...}` - 비디오 공개 시점의 날짜 관련 태그.
* `{media...}` - 미디어 정보 관련 태그.

미디어 관련 태그에는 다음 요소들이 포함됩니다.

* `{media_quality}` - 미디어 화질. (예: `1080p`)
* `{media_video_width}` - 비디오 폭 (픽셀 단위). (예: `1920`)
* `{media_video_height}` - 비디오 높이 (픽셀 단위). (예: `1080`)
* `{media_video_framerate}` - 비디오 프레임 레이트 (fps). (예: `60.0`)
* `{media_bitrate}` - 비트레이트 (bps). (예: `81920000`)
* `{media_video_codec}` - 비디오 코덱. (예: `H264`)

날짜 관련 태그의 세부 요소는 아래와 같이 확장할 수 있습니다.

* `{..._date}` - `%Y%m%d%H%M%S` 형식의 날짜. (예: `20240607014327`)
* `{..._date_year}` 또는 `{..._date_year_full}` - 세기를 포함한 연도. (예: `2024`)
* `{..._date_year_short}` - 세기를 제외한 두 자리 수 연도. (예: `24`)
* `{..._date_month}` - 두 자리 수 월. (`01`, `02`, ..., `12`)
* `{..._date_month_full}` - 월의 전체 이름. (`January`, `February`, ..., `December`)
* `{..._date_month_short}` - 월의 약어. (`Jan`, `Feb`, ..., `Dec`)
* `{..._date_day}` - 두 자리 수 일. (`01`, `02`, ..., `31`)
* `{..._date_hour}` - 두 자리 수 시 (24시간제). (`00`, `01`, ..., `23`)
* `{..._date_minute}` - 두 자리 수 분. (`00`, `01`, ..., `59`)
* `{..._date_second}` - 두 자리 수 초. (`00`, `01`, ..., `59`)

## 미리보기 이미지 처리
미리보기 이미지를 별도로 저장하려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --thumb
```

미리보기 이미지를 저장하지 않으려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --thumb skip
```

## 다운로드 세부 정보 표시 방법 설정
기본적으로 자세한 다운로드 세부 정보가 표시됩니다. 하지만 세부 정보가 필요하지 않은 경우, 다음 명령어를 사용하여 표시를 방지할 수 있습니다.

```powershell
ChzzkVideoDownloader video_no 또는 url -d quiet
ChzzkVideoDownloader video_no 또는 url --display quiet
```

`--display` 매개 변수의 선택 사항을 사용하여 다음과 같은 표시 방법을 설정할 수 있습니다.

* `quiet` - 모든 다운로드 세부 정보 표시를 하지 않습니다.
* `fluent` - 모든 다운로드 세부 정보를 표시합니다.
* `default` - 이 선택 사항은 `fluent`와 동일합니다.

이 선택 사항을 기본값으로 되돌리려면 형식 없이 `-d` 또는 `--display`만 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url -d
ChzzkVideoDownloader video_no 또는 url --display
```

## 작업 디렉터리 설정
올바르게 작동하는데 필요한 파일을 저장할 디렉터리를 지정하려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --work work
```

이 선택 사항을 기본값으로 되돌리려면 디렉터리 없이 `--work`만 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --work
```

## 저장 디렉터리 설정
다운로드된 파일을 저장할 디렉터리를 지정하려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --out out
```

기본적으로 모든 파일은 스트리머별 하위 디렉터리에 분류하여 저장됩니다. 만약 스트리머별로 분류하지 않고 저장하려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --category none
```

이 선택 사항을 기본값으로 되돌리려면 디렉터리 없이 `--out`과 `-category`만 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --out --category
```

## 임시 디렉터리 설정
다운로드 중인 파일을 저장할 임시 디렉터리를 지정하려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --temp temp
```

이 선택 사항을 기본값으로 되돌리려면 디렉터리 없이 `--temp`만 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --temp
```

## 파일이 이미 존재할 때 파일 저장 방법 설정
기본적으로 저장하려는 파일과 동일한 이름의 파일이 이미 존재할 때, 파일 이름 뒤에 `(n)`을 붙여 저장합니다. 하지만 다음 명령어를 사용하여 파일을 덮어쓰거나 다운로드 자체를 건너뛰도록 지정할 수 있습니다.

```powershell
ChzzkVideoDownloader video_no 또는 url --exist overwrite
ChzzkVideoDownloader video_no 또는 url --exist skip
```

이 선택 사항을 기본값으로 되돌리려면 설정 없이 `--exist`만 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --exist
```

## 여유 저장 공간이 임계점 이하로 낮아질 때 다운로드 중지 설정
기본적으로, 저장 디렉터리와 임시 디렉터리의 여유 공간이 10% 이하로 낮아질 때 다운로드를 중지합니다. 여유 저장 공간의 임계점을 설정하려면 다음 명령어를 사용하세요. 이 때 설정 가능한 값은 3부터 30까지입니다.

```powershell
ChzzkVideoDownloader video_no 또는 url --threshold 20
```

여유 저장 공간에 따른 다운로드 중지 기능을 비활성화하려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --threshold -
```

이 선택 사항을 기본값으로 되돌리려면 설정 없이 `--threshold`만 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --threshold
```

## 다운로드 방법 설정
대체 다운로드 모듈이 포함되어 있습니다. 대체 모듈을 사용해 보려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --download alter
```

## 설정 저장 시 동작 설정
모든 선택 사항은 기본적으로 항상 설정 파일에 저장됩니다. 현재 세션에만 설정을 적용하고 저장하지 않으려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader video_no 또는 url --settings skip
```

단, 다음 정보는 항상 저장됩니다.

* 치지직 쿠키에서 얻은 NAVER ID 인증 키 (`NID_AUT`)
* 치지직 쿠키에서 얻은 NAVER ID 세션 키 (`NID_SES`)

다운로드 없이 설정만 저장하고 종료하려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader --settings quit
```

## 모든 설정 초기화
사용 시간이 길어질수록 설정이 꼬일 수 있습니다. 모든 설정을 초기화하려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader --reset
```

다음 정보가 초기화됩니다.

* Chzzk 쿠키에서 얻은 NAVER ID 인증 키 (`NID_AUT`)
* Chzzk 쿠키에서 얻은 NAVER ID 세션 키 (`NID_SES`)
* 다운로드할 목표 화질 설정
* 미리보기 이미지 저장 설정
* 다운로드 세부 정보 표시 설정
* 출력 및 임시 디렉터리 설정

## 버전 정보 표시
다음 명령어를 사용하여 버전 정보를 확인할 수 있습니다.

```powershell
ChzzkVideoDownloader --version
```

## 도움말 확인
간단한 매개 변수 도움말을 확인하려면 다음 명령어를 사용하세요.

```powershell
ChzzkVideoDownloader -h
ChzzkVideoDownloader --help
```

## 매개 변수 우선 순위
`--reset`, `-h`, `--version`을 제외한 매개 변수는 아래 예시와 같이 순서에 상관없이 사용할 수 있습니다. 단, 동일한 매개 변수를 중복으로 지정할 수는 없습니다.

```powershell
ChzzkVideoDownloader 1602969 --out out
```

`-h`와 `--version` 매개 변수는 첫 번째로 사용된 것만 처리되고 즉시 종료됩니다. 따라서 아래 명령어는 버전 정보만 출력됩니다.

```powershell
ChzzkVideoDownloader --version -h
```

`--reset` 매개 변수는 설정을 초기화하고 이전에 설정된 값을 무시한 후 종료됩니다. 따라서 다음 명령어에서 비디오 번호는 무시됩니다.

```powershell
ChzzkVideoDownloader 1602969 --reset
```

## 권장 초기 설정
처음 사용할 때는 다음 설정을 권장합니다. 다음 명령어를 사용하면 작업 디렉터리(`--work`), 저장 디렉터리(`--out`), 임시 디렉터리(`--temp`)를 한 번에 설정하여 다운로드한 비디오 파일을 정리하기 쉽게 만듭니다.

```powershell
ChzzkVideoDownloader video_no 또는 url --work work --out out --temp temp
```

## JSON-RPC를 사용한 외부 제어
자세한 정보는 `how_to_control_chzzk_video_downloader.ko-KR.pdf` 파일을 참조하세요.

## 문의하기
치지직 다운로드 도구에 대해 궁금한 사항, 제보할 오류, 개선 요청 사항 등이 있을 때는 [GitHub](https://github.com/Choonholic/ChzzkDownloader/)의 [Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new) 기능을 통해 제보해 주세요. 모든 언어에 대응 가능하나, 직접 대응 가능한 언어는 한국어, 영어, 일본어, 중국어이며, 다른 언어는 기계 번역을 통하기 때문에 100% 대응이 불가능할 수 있습니다.
