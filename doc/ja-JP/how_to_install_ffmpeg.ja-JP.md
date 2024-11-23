# Windowsでのffmpegインストール方法

* FFmpegのサポートされる最小バージョンは7.0です。
* FFmpegが既にインストールされている場合、以下の手順を実行する必要はなく、システム環境変数のPathにFFmpegがインストールされているディレクトリのパスを追加するだけで構いません。

1. **PowerShell**を開きます。
2. 次のコマンドを実行します。

```powershell
winget install --id gyan.FFmpeg --source winget
```

3. インストールが完了したら、設定とシステム環境を適用するためにコンピューターを再起動します。
