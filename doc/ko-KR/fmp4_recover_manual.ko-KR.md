# fMP4 Recover

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_fmp4recover.png' />
<p><i>(이 이미지는 최신 정보와 다를 수 있습니다.)</i></p>
</div>

fMP4 Recover는 다운로드한 Fragmented MP4 (fMP4) 파일의 일부 세그먼트가 손상된 경우 가능한 범위에서 영상 데이터를 복구하기 위한 실험적 복구 도구입니다.

파일 내부의 세그먼트를 분석하여 정상적인 미디어 데이터를 최대한 복구한 후 새로운 MP4 파일을 생성합니다.

## 선행 요건

fMP4 Recover를 사용하려면 FFmpeg 및 FFprobe가 설치되어 있어야 합니다.

설치 방법은 `how_to_install_ffmpeg.ko-KR.pdf`를 참조해 주세요.

## 사용 방법

`fMP4Recover.exe`를 복구할 파일과 함께 실행합니다.

```
.\fMP4Recover.exe "video.ts"
```

복구할 파일을 `fMP4Recover.exe`에 끌어다 놓아 실행할 수도 있습니다.

복구가 완료되면 다음과 같이 원본 파일 이름 뒤에 `_fixed`가 추가된 새로운 파일이 같은 디렉터리에 생성됩니다. 이때 원본 파일은 변경되지 않으며 복구가 정상적으로 이루어진 것을 확인했다면 삭제하셔도 무방합니다.

```
video.ts
video_fixed.mp4
```

## 제한사항

fMP4 Recover는 현재 확인된 특정 형태의 Fragmented MP4 파일 손상을 복구하기 위한 도구입니다. 분석된 형태와 다른 원인으로 손상되었거나 파일 구조 또는 손상 형태가 다른 경우에는 복구할 수 없습니다.

또한 복구할 수 없는 세그먼트는 결과 파일에서 제거되므로 해당 구간의 영상이나 음성이 일부 누락될 수 있습니다.

원본 파일에 충분한 정상 미디어 데이터가 남아 있는 경우에만 복구할 수 있습니다. 복구된 MP4 파일이 정상적인지 확인할 때까지 원본 파일을 보관해 주세요.
