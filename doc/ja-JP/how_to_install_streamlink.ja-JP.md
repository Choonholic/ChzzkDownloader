# WindowsでのStreamlinkインストール方法

Streamlinkのインストール方法は、システム全体から利用できるPython環境があるかどうかによって異なります。

## 1. pipを使用したインストール（Python環境がある場合）

**最低サポートバージョン：8.6.1**

システム全体から利用できるPython環境がある場合は、`pip`を使用してStreamlinkをインストールまたは更新できます。

```powershell
python -m pip install --upgrade streamlink
```

Python開発者（いわゆるPythonista）の方は、普段使用しているPython環境を利用できます。

## 2. Pythonを使用しないインストール

**最低サポートバージョン：8.3.0**

Pythonがインストールされていない場合は、Pythonランタイムが同梱されたWindows用インストーラーを使用できます。

1. [streamlink-8.6.3-1-py315-x86_64.exe](https://github.com/streamlink/windows-builds/releases/download/8.6.3-1/streamlink-8.6.3-1-py315-x86_64.exe)をダウンロードします。
2. ダウンロードしたインストーラーを実行します。
3. インストール対象のユーザーを選択する画面では、**Install for anyone using this computer**を選択します。
4. インストール完了後、システム環境設定の変更を確実に反映させるため、コンピューターを再起動します。

## セキュリティに関する推奨事項

**インストール方法にかかわらず、潜在的なセキュリティリスクを最小限に抑え、互換性と安定性を確保するため、Streamlinkを常に利用可能な最新バージョンに更新することを強く推奨します。**
