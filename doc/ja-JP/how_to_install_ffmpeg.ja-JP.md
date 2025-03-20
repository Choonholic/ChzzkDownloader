# Windowsでのffmpegインストール方法

## お知らせ

* FFmpegのサポートされる最小バージョンは7.0です。
* FFmpegが既にインストールされている場合、以下の手順を実行する必要はなく、システム環境変数のPathにFFmpegがインストールされているディレクトリのパスを追加するだけで構いません。

## インストーラーを使用してインストールする

* 注意：この方法でインストールされたバイナリは、最新バージョンがすぐに反映されない場合があります。

1. [https://getffmpeg.org/](https://getffmpeg.org/) のウェブページを開きます。
2. **Download ffmpeg-setup.exe Installer**ボタンをクリックして、`ffmpeg-setup.exe`ファイルをダウンロードします。
3. `ffmpeg-setup.exe`ファイルを実行し、指示に従ってインストールを完了します。

## Wingetを使用して最新バージョンをインストールする

1. **PowerShell**を開きます。
2. 次のコマンドを実行します。

```powershell
winget install --id gyan.FFmpeg --source winget
```

3. インストールが完了したら、設定とシステム環境を適用するためにコンピューターを再起動します。
