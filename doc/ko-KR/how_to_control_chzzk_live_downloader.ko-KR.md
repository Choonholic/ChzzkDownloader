# Chzzk Live Downloader 외부 제어 방법 (JSON-RPC 사용)

## Chzzk Downloader Suite JSON-RPC 사양
Chzzk Downloader Suite를 외부에서 제어하기 위해 단일 요청 방식의 [JSON-RPC 2.0 사양](https://www.jsonrpc.org/specification)을 지원합니다.

## 서버 활성화 방법
Chzzk Live Downloader를 실행할 때 `--rpc` 선택 사항을 지정합니다.

## 서버 연결 방법
내부 JSON-RPC 서버는 소켓 연결을 허용합니다.

* **호스트 IP 주소** - 기본 주소는 `localhost`입니다.
* **포트 번호** - 기반 포트 번호 (기본값: `62000`) + 스트리머 ID입니다. `--rpcbaseport` 선택 사항을 사용해 변경할 수 있습니다. (사용 가능 범위: `49152`~`65300`)
* **RPC ID** - 별도 지정 없이 스트리머 ID를 사용합니다. `-i` 선택 사항을 사용해 변경할 수 있습니다. (기본값: `0`)

스트리머 아이디가 `3`일 경우, 기본적으로 포트 번호는 `62003`이 됩니다.

## 요청 방법
Chzzk Live Downloader에 작업을 요청하려면, 아래와 같은 객체를 소켓을 통해 전송합니다.

```json
{
    "jsonrpc": "2.0",
    "method": "get_status",
    "id": 1
}
```

### 메서드 목록
* `get_info` - 모든 정보를 한 번에 가져옵니다.
* `get_version` – 애플리케이션 버전을 가져옵니다.
* `get_settings` – 애플리케이션 설정을 가져옵니다.
* `get_channel` – 채널 정보를 가져옵니다.
* `get_status` – 현재 상태를 가져옵니다.
* `get_live` – 현재 라이브 스트리밍을 다운로드 중이라면 해당 라이브 스트리밍 정보를 가져옵니다.
* `skip_current` - 현재 스트리밍의 다운로드를 건너뛰고 다음 스트리밍을 기다립니다.
* `stop_current` - 현재 스트리밍의 다운로드를 중지하고 다음 스트리밍을 기다립니다.
* `resume_download` - 중지했던 라이브 스트리밍의 다운로드를 다시 시작합니다.
* `set_settings` – 애플리케이션 설정을 변경합니다.
* `reload_settings` – 설정 파일에서 애플리케이션 설정을 다시 읽습니다.
* `quit_app` – (현재 다운로드를 진행 중이라면) 진행 중인 다운로드를 중지하고 애플리케이션을 종료합니다.

## 응답 형식
Chzzk Live Downloader는 다음과 같은 형식으로 응답을 반환합니다.

```json
{
    "jsonrpc": "2.0",
    "result": "Success",
    "id": 1
}
```

### 요청이 성공적으로 처리된 경우
* `result` - 요청된 메서드의 결과를 나타냅니다.

### 요청이 정상적으로 처리되지 않은 경우
* `error` - 오류 응답임을 나타냅니다.
* `code` - 오류 코드.
* `message` - 오류 메시지.

## 예제 코드
예제 코드는 GitHub 저장소의 [samples](https://github.com/Choonholic/ChzzkDownloader/blob/main/samples/)에서 확인하실 수 있습니다.
