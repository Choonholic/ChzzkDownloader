# Windows 버전 ffmpeg 설치하기

## 알림

* Chzzk Downloader Suite는 공식 메이저 버전(Official Major Version)의 FFmpeg만 지원하며, 테스트 빌드를 비롯한 비정기 빌드는 지원하지 않습니다.
* 지원 가능한 FFmpeg의 최소 버전은 7.0입니다.
* 만약 FFmpeg이 이미 설치되어 있다면, 다음 단계를 실행할 필요 없이 시스템 환경 변수 중 Path에 FFmpeg이 설치되어 있는 경로를 추가하면 준비가 완료됩니다.

## 설치 프로그램을 이용하여 설치하기

* 주의: 이 방법으로 설치하는 바이너리는 최신 버전의 반영이 바로 이루어지지 않을 수 있습니다.

1. [https://getffmpeg.org/](https://getffmpeg.org/) 웹페이지를 엽니다.
2. **Download ffmpeg-setup.exe Installer** 버튼을 클릭하여 `ffmpeg-setup.exe` 파일을 다운로드합니다.
3. `ffmpeg-setup.exe` 파일을 실행하여 지침에 따라 설치를 완료합니다.

## Winget을 이용하여 최신 버전 설치하기

1. `PowerShell`을 실행합니다.
2. 아래 명령어를 실행합니다.

```powershell
winget install --id Gyan.FFmpeg --source winget
```

3. 설치가 완료되면, 설정이 시스템 환경에 적용될 수 있도록 장치를 재시작합니다.
