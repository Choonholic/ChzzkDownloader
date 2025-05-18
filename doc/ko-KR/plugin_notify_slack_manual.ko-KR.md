# Slack 알림 플러그인

메시지를 Slack 사용자에게 전달하는 플러그인입니다.

## 초기 설정하기

### Webhook URL 만들기

1. [Slack API: Incoming Webhooks](https://api.slack.com/messaging/webhooks) 페이지에 접속합니다.
2. **Create your Slack app**을 클릭하여 새 앱을 만듭니다.
3. 앱 이름과 연결할 워크스페이스를 선택한 후 **Create App**을 클릭합니다.
4. 왼쪽 메뉴에서 **Incoming Webhooks**를 클릭하고, **Activate Incoming Webhooks**를 **On**으로 설정합니다.
5. 페이지 하단의 **Add New Webhook to Workspace**를 클릭하고, 메시지를 전송할 채널을 선택한 후 **Allow**를 클릭합니다.
6. 생성된 **Webhook URL**이 화면에 표시됩니다. 이 URL을 복사하여 안전한 곳에 보관합니다.

### 플러그인 초기화하기

1. `pn_slack.exe` 파일이 있는 디렉터리에 `pn_slack.json` 파일이 이미 존재한다면, 해당 파일의 이름을 `pn_slack.json.bak`으로 변경하거나 삭제합니다.
2. `pn_slack.exe` 파일을 실행합니다.
3. `Please enter your Slack webhook URL:` 메시지가 출력되면 앞의 **Webhook URL 만들기** 단계에서 복사한 URL을 붙여넣습니다.

## 테스트하기
명령 프롬프트 또는 PowerShell에서 다음 명령을 실행하여 메시지가 올바르게 전송되는지 확인합니다.

```powershell
.\pn_slack.exe "메시지 전송 테스트"
```

## 제약 사항
이 플러그인은 `plain` 또는 `slack` 알림 텍스트 형식만 지원합니다.
