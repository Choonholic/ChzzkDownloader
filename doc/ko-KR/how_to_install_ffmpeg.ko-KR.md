# Windows 버전 ffmpeg 설치하기

* 지원 가능한 FFmpeg의 최소 버전은 7.0입니다.
* 만약 FFmpeg이 이미 설치되어 있다면, 다음 단계를 실행할 필요 없이 시스템 환경 변수 중 Path에 FFmpeg이 설치되어 있는 경로를 추가하면 준비가 완료됩니다.

1. `PowerShell`을 실행합니다.
2. 아래 명령어를 실행합니다.

```powershell
winget install --id gyan.FFmpeg --source winget
```

3. 설치가 완료되면, 설정이 시스템 환경에 적용될 수 있도록 장치를 재시작합니다.
