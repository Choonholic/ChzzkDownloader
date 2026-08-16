# WindowsでFFmpegをインストールする方法

## お知らせ

- Chzzk Downloader SuiteはFFmpegの公式メジャーバージョンのみをサポートしており、テストビルドやその他の非公式リリースはサポートしていません。
- サポートされるFFmpegの最低バージョンは7.0です。
- FFmpegがすでにインストールされている場合は、以下の手順を省略し、`ffmpeg.exe`が含まれているディレクトリをシステム環境変数`PATH`に追加するだけで使用できます。

## インストーラーを使用してインストールする

- 注意：この方法でインストールされるバイナリは、最新バージョンがすぐに反映されない場合があります。

1. [https://getffmpeg.org/](https://getffmpeg.org/)を開きます。
2. **Download ffmpeg-setup.exe Installer**ボタンをクリックして、`ffmpeg-setup.exe`ファイルをダウンロードします。
3. `ffmpeg-setup.exe`ファイルを実行し、画面の指示に従ってインストールを完了します。

## Wingetを使用して最新バージョンをインストールする

1. `PowerShell`を開きます。
2. 以下のコマンドを実行します。

   ```powershell
   winget install --id Gyan.FFmpeg --source winget
   ```

3. インストールが完了したら、設定およびシステム環境を反映するためにコンピューターを再起動します。

## 公式ビルドを手動でインストールする

1. [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)を開きます。
2. **release builds**の**latest release**セクションから、以下のファイルのいずれかをダウンロードします。

   * `ffmpeg-release-essentials.7z`
   * `ffmpeg-release-essentials.zip`
   * `ffmpeg-release-full.7z`
   * `ffmpeg-release-full-shared.7z`

3. ダウンロードしたアーカイブを任意のディレクトリに展開します。
4. 展開したFFmpegディレクトリ内の`bin`ディレクトリをシステム環境変数`PATH`に追加します。

   ディレクトリを`PATH`環境変数に追加する方法については、`how_to_add_path_environment.ja-JP.pdf`を参照してください。
