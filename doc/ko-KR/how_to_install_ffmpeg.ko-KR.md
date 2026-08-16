# Windows 버전 FFmpeg 설치하기

## 주의 사항

- Chzzk Downloader Suite는 FFmpeg의 공식 메이저 버전(Official Major Version)만 지원하며, 테스트 빌드나 기타 비공식 릴리스는 지원하지 않습니다.
- 지원되는 FFmpeg의 최소 버전은 7.0입니다.
- FFmpeg가 이미 설치되어 있다면 아래 단계를 생략하고 `ffmpeg.exe`가 포함된 디렉터리를 `PATH` 시스템 환경 변수에 추가하기만 하면 됩니다.

## 설치 프로그램을 사용하여 설치하기

- 참고: 이 방법으로 설치되는 바이너리는 최신 버전이 즉시 반영되지 않을 수 있습니다.

1. [https://getffmpeg.org/](https://getffmpeg.org/)를 엽니다.
2. **Download ffmpeg-setup.exe Installer** 버튼을 클릭하여 `ffmpeg-setup.exe` 파일을 다운로드합니다.
3. `ffmpeg-setup.exe` 파일을 실행하고 화면의 안내에 따라 설치를 완료합니다.

## Winget을 사용하여 최신 버전 설치하기

1. `PowerShell`을 엽니다.
2. 다음 명령을 실행합니다.

   ```powershell
   winget install --id Gyan.FFmpeg --source winget
   ```

3. 설치가 완료되면 설정 및 시스템 환경을 적용하기 위해 컴퓨터를 다시 시작합니다.

## 공식 빌드를 수동으로 설치하기

1. [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)를 엽니다.
2. **release builds**의 **latest release** 섹션에서 다음 파일 중 하나를 다운로드합니다.

   * `ffmpeg-release-essentials.7z`
   * `ffmpeg-release-essentials.zip`
   * `ffmpeg-release-full.7z`
   * `ffmpeg-release-full-shared.7z`

3. 다운로드한 압축 파일을 원하는 디렉터리에 압축 해제합니다.
4. 압축을 해제한 FFmpeg 디렉터리 안의 `bin` 디렉터리를 `PATH` 시스템 환경 변수에 추가합니다.

   디렉터리를 `PATH` 환경 변수에 추가하는 방법은 `how_to_add_path_environment.ko-KR.pdf`를 참조하세요.
