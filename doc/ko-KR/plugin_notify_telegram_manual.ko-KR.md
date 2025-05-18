# Telegram 알림 플러그인

메시지를 Telegram 사용자에게 전달하는 플러그인입니다.

## 초기 설정하기

### 봇 생성하기

1. Telegram에서 `@BotFather`를 검색하여 대화를 시작합니다.
2. `/newbot`을 입력하여 새로운 봇을 생성합니다.
3. 봇의 이름(name)을 물어보면 봇의 이름을 새로 입력합니다. 이 때 봇의 이름은 다른 봇과 중복될 수 없습니다.
4. 봇의 사용자 이름(username)을 물어보면 봇의 사용자 이름을 새로 입력합니다. 이 때 사용자 이름은 `bot`으로 끝나야 합니다. 이 때 대소문자는 구분하지 않습니다.
5. 생성 완료 안내 메시지에 표시되는 봇의 토큰(token)을 복사하여 안전한 곳에 보관해 둡니다.

### 사용자 ID 확인하기

1. Telegram에서 `@userinfobot`을 검색하여 대화를 시작합니다.
2. `/start`를 입력하여 사용자 정보를 확인합니다.
3. `Id` 값을 복사하여 안전한 곳에 보관해 둡니다.

### 플러그인 초기화하기

1. `pn_telegram.exe` 파일이 있는 디렉터리에 `pn_telegram.json` 파일이 존재할 경우, `pn_telegram.json.bak`으로 이름을 바꾸거나 삭제합니다.
2. `pn_telegram.exe` 파일을 실행합니다.
3. `Please enter your Telegram bot token:` 메시지가 출력되면 앞의 **봇 생성하기** 단계에서 복사한 봇의 토큰을 입력합니다.
4. `Please enter your Telegram chat ID:` 메시지가 출력되면 앞의 **사용자 ID 확인하기** 단계에서 복사한 사용자 아이디를 입력합니다.

## 테스트하기
명령 프롬프트 또는 PowerShell에서 다음 명령을 실행하여 메시지가 올바르게 전송되는지 확인합니다.

```powershell
.\pn_telegram.exe "메시지 전송 테스트"
```

## 제약 사항
이 플러그인은 `plain`, `markdown` 또는 `html` 알림 텍스트 형식만 지원합니다.
