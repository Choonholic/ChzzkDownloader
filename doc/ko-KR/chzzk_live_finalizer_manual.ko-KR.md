# Chzzk Live Finalizer
치지직 라이브 스트리밍 최종 처리 도구

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_chzzklivefinalizer.png' />
<p><i>(이 이미지는 최신 정보와 다를 수 있습니다.)</i></p>
</div>

## 버전
Version 1.5.2, December 30, 2024 00:00:00

## 사용법
```powershell
ChzzkLiveFinalizer [-h] [--version] [-d [DISPLAY]] [--work [WORK]] [--work-user [WORK_USER]]
                   [--work-pass [WORK_PASS]] [--watch [WATCH]] [--watch-user [WATCH_USER]]
                   [--watch-pass [WATCH_PASS]] [--convert [CONVERT]] [--exist [EXIST]]
                   [--threshold [THRESHOLD]] [--rpcid [RPCID]] [--rpcport [RPCPORT]]
                   [--snapshot SNAPSHOT] [--startup [STARTUP]] [--settings [SETTINGS]] [--reset]
```

## 선택적 매개 변수
```
-h, --help                도움말 페이지를 표시합니다
--version                 버전 정보를 표시합니다
-d, --display [DISPLAY]   처리 상태 표시 모드를 설정합니다 (quiet|simple|fluent|all)
--work [WORK]             작업 디렉터리를 설정합니다
--work-user [WORK_USER]   작업 디렉터리가 네트워크 공간에 있을 떄 사용할 사용자 이름을 설정합니다
--work-pass [WORK_PASS]   작업 디렉터리가 네트워크 공간에 있을 떄 사용할 비밀번호를 설정합니다
--watch [WATCH]           감시 디렉터리를 설정합니다.
--watch-user [WATCH_USER] 감시 디렉터리가 네트워크 공간에 있을 떄 사용할 사용자 이름을 설정합니다
--watch-pass [WATCH_PASS] 감시 디렉터리가 네트워크 공간에 있을 떄 사용할 비밀번호를 설정합니다
--convert [CONVERT]       변환 매개 변수를 설정합니다
--exist [EXIST]           파일이 이미 존재할 때 파일 저장 방법을 설정합니다 (rename|skip|overwrite)
--threshold [THRESHOLD]   디스크 공간 부족 시 중지 임계값(%)을 설정합니다 (비활성화: -, 기본값: 10, 3-30)
--rpcid [RPCID]           JSON-RPC 서버 ID를 설정합니다 (기본값: 70)
--rpcport [RPCPORT]       JSON-RPC 서버 포트를 설정합니다 (기본값: 65000, 49152-65300)
--snapshot SNAPSHOT       상태 변경 시 스냅샷을 JSON 파일로 저장합니다
--startup [STARTUP]       시작 방법을 설정합니다 (normal|fast)
--settings [SETTINGS]     설정 저장 시 동작을 설정합니다 (default|skip|quit)
--reset                   모든 설정을 초기화합니다
```

## 사용 예시
```powershell
ChzzkLiveFinalizer --work work --watch out
```

## 설명
Chzzk Live Finalizer는 Chzzk Live Downloader가 직접 최종 처리를 진행하는 대신, 별도 프로세스에서 순차적으로 최종 처리를 진행하도록 설계된 도구입니다. Chzzk Live Finalizer를 사용하면 라이브 스트림이 짧은 간격으로 방송되더라도 영향 없이 다운로드할 수 있도록 도와 줍니다.

## 작업 디렉터리 설정
올바르게 작동하는데 필요한 파일을 저장할 디렉터리를 지정하려면 다음 명령어를 사용하세요.

```powershell
ChzzkLiveFinalizer --work work
```

이 선택 사항을 기본값으로 되돌리려면 디렉터리 없이 `--work`만 사용하세요.

```powershell
ChzzkLiveFinalizer --work
```

## 감시 디렉터리 설정
Chzzk Live Finalizer는 스트림 파일이 저장되는 디렉터리를 감시하다가, 파일이 새로 추가되면 자동으로 최종 변환을 진행합니다. 다음 명령어를 사용하면 감시 디렉터리를 지정할 수 있습니다.

```powershell
ChzzkLiveFinalizer --watch out
```

이 선택 사항을 기본값으로 되돌리려면 디렉터리 지정 없이 `--watch`만 사용하세요.

```powershell
ChzzkLiveFinalizer --watch
```

## 디렉터리 지정 방법
디렉터리는 다음과 같이 여러 가지 방법으로 지정할 수 있습니다.

```powershell
ChzzkLiveFinalizer --work work
```

실행 파일이 있는 디렉터리의 하위 디렉터리인 `work`를 작업 디렉터리로 지정합니다. 해당 디렉터리가 존재하지 않으면 새로 생성됩니다.

```powershell
ChzzkLiveFinalizer --watch \Users\Username\Documents\chzzk
```

현재 드라이브의 `C:\Users\Username\Documents\chzzk`을 감시 디렉터리로 지정합니다. 해당 디렉터리가 존재하지 않으면 새로 생성됩니다.

```powershell
ChzzkLiveFinalizer --watch C:\Users\Username\Documents\chzzk
```

물론 위와 같이 직접 드라이브(예: `C:`)를 지정할 수도 있습니다.

```powershell
ChzzkLiveFinalizer --watch \\192.168.0.1\chzzk
```

UNC 경로 기반인 `\\192.168.0.1\chzzk\chzzk` 네트워크 저장 공간을 감시 디렉터리로 지정합니다. 해당 디렉터리가 존재하지 않으면 새로 생성됩니다.

네트워크 저장 공간에 파일을 저장할 때는 사용자 이름과 비밀번호를 입력해야 할 수 있습니다. 이 정보는 다음과 같이 지정할 수 있습니다.

```powershell
ChzzkLiveFinalizer --work-user username --work-pass password
ChzzkLiveFinalizer --watch-user username --watch-pass password
```

### 최종 처리 인코딩 매개 변수 설정
`--convert` 선택 사항을 사용하여 최종 처리에 사용할 인코딩 매개 변수를 설정할 수 있습니다. 예를 들어, 다음 설정은 `FFmpeg`을 사용하여 `H.265` 코덱으로 인코딩하도록 설정합니다:

```powershell
ChzzkLiveFinalizer --convert "-c:v libx265 -preset medium -crf 23 -c:a aac -b:a 128k"
```

이 선택 사항을 기본값으로 되돌리려면 다음과 같이 `--convert`만 사용하세요.

```powershell
ChzzkLiveFinalizer --convert
```

## 처리 정보 표시 방법 설정
기본적으로 자세한 세부 처리 정보가 표시됩니다. 하지만 세부 정보가 필요하지 않은 경우, 다음 명령어를 사용하여 표시를 방지할 수 있습니다.

```powershell
ChzzkLiveFinalizer -d quiet
ChzzkLiveFinalizer --display quiet
```

`--display` 매개 변수의 선택 사항을 사용하여 다음과 같은 표시 방법을 설정할 수 있습니다.

* `quiet` - 모든 세부 처리 정보 표시를 하지 않습니다.
* `fluent` - 모든 세부 처리 정보를 표시합니다.
* `default` - 이 선택 사항은 `fluent`와 동일합니다.

이 선택 사항을 기본값으로 되돌리려면 형식 없이 `-d` 또는 `--display`만 사용하세요.

```powershell
ChzzkLiveFinalizer -d
ChzzkLiveFinalizer --display
```

## 파일이 이미 존재할 때 파일 저장 방법 설정
기본적으로 저장하려는 파일과 동일한 이름의 파일이 이미 존재할 때, 파일 이름 뒤에 `(n)`을 붙여 저장합니다. 하지만 다음 명령어를 사용하여 파일을 덮어쓰거나 최종 처리 자체를 건너뛰도록 지정할 수 있습니다.

```powershell
ChzzkLiveFinalizer --exist overwrite
ChzzkLiveFinalizer --exist skip
```

이 선택 사항을 기본값으로 되돌리려면 설정 없이 `--exist`만 사용하세요.

```powershell
ChzzkLiveFinalizer --exist
```

## 여유 저장 공간이 임계점 이하로 낮아질 때 최종 변환 중지 설정
기본적으로, 저장 디렉터리와 임시 디렉터리의 여유 공간이 10% 이하로 낮아질 때 최종 변환을 중지합니다. 여유 저장 공간의 임계점을 설정하려면 다음 명령어를 사용하세요. 이 때 설정 가능한 값은 `3`부터 `30`까지입니다.

```powershell
ChzzkLiveFinalizer --threshold 20
```

여유 저장 공간에 따른 최종 처리 중지 기능을 비활성화하려면 다음 명령어를 사용하세요.

```powershell
ChzzkLiveFinalizer --threshold -
```

이 선택 사항을 기본값으로 되돌리려면 설정 없이 `--threshold`만 사용하세요.

```powershell
ChzzkLiveFinalizer --threshold
```

## 설정 저장 시 동작 설정
모든 선택 사항은 기본적으로 항상 설정 파일에 저장됩니다. 현재 세션에만 설정을 적용하고 저장하지 않으려면 다음 명령어를 사용하세요.

```powershell
ChzzkLiveFinalizer --settings skip
```

다운로드 없이 설정만 저장하고 종료하려면 다음 명령어를 사용하세요.

```powershell
ChzzkLiveFinalizer --settings quit
```

## 모든 설정 초기화
사용 시간이 길어질수록 설정이 꼬일 수 있습니다. 모든 설정을 초기화하려면 다음 명령어를 사용하세요.

```powershell
ChzzkLiveFinalizer --reset
```

다음 정보가 초기화됩니다.

* 세부 처리 정보 표시 설정
* 감시할 디렉터리 설정
* 변환 매개 변수 설정

## 버전 정보 표시
다음 명령어를 사용하여 버전 정보를 확인할 수 있습니다.

```powershell
ChzzkLiveFinalizer --version
```

## 도움말 확인
간단한 매개 변수 도움말을 확인하려면 다음 명령어를 사용하세요.

```powershell
ChzzkLiveFinalizer -h
ChzzkLiveFinalizer --help
```

## 매개 변수 우선 순위
`--reset`, `-h`, `--version`을 제외한 매개 변수는 아래 예시와 같이 순서에 상관없이 사용할 수 있습니다. 단, 동일한 매개 변수를 중복으로 지정할 수는 없습니다.

```powershell
ChzzkLiveFinalizer -d quiet --watch out
```

`-h`와 `--version` 매개 변수는 첫 번째로 사용된 것만 처리되고 즉시 종료됩니다. 따라서 아래 명령어는 버전 정보만 출력됩니다.

```powershell
ChzzkLiveFinalizer --version -h
```

`--reset` 매개 변수는 설정을 초기화하고 이전에 설정된 값을 무시한 후 종료됩니다. 따라서 다음 명령어에서 `--watch` 매개 변수는 무시됩니다.

```powershell
ChzzkLiveFinalizer --watch out --reset
```

## JSON-RPC를 사용한 외부 제어
자세한 정보는 `how_to_control_chzzk_live_finalizer.ko-KR.pdf` 파일을 참조하세요.

## 문의하기
치지직 다운로드 도구에 대해 궁금한 사항, 제보할 오류, 개선 요청 사항 등이 있을 때는 [GitHub](https://github.com/Choonholic/ChzzkDownloader/)의 [Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new) 기능을 통해 제보해 주세요. 모든 언어에 대응 가능하나, 직접 대응 가능한 언어는 한국어, 영어, 일본어, 중국어이며, 다른 언어는 기계 번역을 통하기 때문에 100% 대응이 불가능할 수 있습니다.