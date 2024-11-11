# Chzzk Video Manager
Chzzk Video Downloader用のGUIマネージャー

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_chzzkvideomanager.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

## バージョン
Version 0.95, November 12, 2024 00:00:00

## 必要条件
Chzzk Video Managerは、Chzzk Video DownloaderのGUIフロントエンドアプリケーションであるため、Chzzk Video Downloaderもインストールされている必要があります。

Chzzk Video DownloaderとChzzk Video Managerが同じディレクトリにある場合、Chzzk Video Managerは起動時に自動的にChzzk Video Downloaderを認識します。そうでない場合は、**必要条件の確認**を参照して、Chzzk Video Downloaderの場所を指定してください。

ポータブル版の場合は、Chzzk Video DownloaderとChzzk Video Managerを同じディレクトリに保存することをお勧めします。`セットアップ`を使用してインストールした場合、両方が同じディレクトリにインストールされます。

## 実行方法
スタートメニューから`Chzzk Video Manager`をクリックするか、`Chzzk Downloader Environment`で`ChzzkVideoManager.exe`を実行します。

## 必要条件の確認
Chzzk Video Managerが正常に機能するためには、Chzzk Video Downloaderが正しく設定されている必要があります。Chzzk Video Managerの起動時に、この必要条件が満たされているかチェックし、満たされていない場合は、以下のダイアログが表示されます。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_prerequisites.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

`設定...`ボタンをクリックしてChzzk Video Downloaderの場所を指定できます。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_downloader_locate_01.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

`...`ボタンをクリックして、正しいパスにある`ChzzkVideoDownloader.exe`ファイルを選択してください。正しいChzzk Video Downloaderが指定されると、以下の図のようにバージョン情報が表示されます。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_downloader_locate_02.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

## メインメニューを開く
ウィンドウの左上にある☰アイコンをクリックすると、メインメニューが開きます。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_main_menu.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

## ビデオの追加
メインメニューから`ビデオの追加...`を選択すると、ビデオ追加ダイアログが表示されます。追加するビデオ番号またはURLを入力し、`OK`ボタンをクリックしてビデオを追加します。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_add_video.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

### ビデオ番号またはURL
入力されたビデオ番号は、次のいずれかの形式として自動的に認識されます。

* ビデオURL - `https://chzzk.naver.com/video/number`
* ビデオ番号 - `number`

## ビデオの削除
ビデオを削除するには、リストからビデオを選択し、☰アイコンをクリックして`ビデオの削除`を選択し、確認のため`OK`をクリックします。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_remove_video.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

## ダウンロードの開始
リストのビデオのダウンロードを開始するには、☰アイコンをクリックし、`ダウンロード開始`を選択します。

## ダウンロードの停止
リストのビデオのダウンロードを停止するには、☰アイコンをクリックし、`ダウンロード停止`を選択し、確認のため`OK`をクリックします。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_stop_download.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

ダウンロードを停止すると、進行中のすべてのダウンロードが中断されます。

## ビデオのプロパティの表示
ビデオのプロパティを参照するには、リストからビデオを選択し、☰アイコンをクリックして`プロパティ...`を選択します。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_properties.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

## コンテキストメニュー
リストからビデオを選択して右クリックすると、ビデオのコンテキストメニューが表示されます。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_context_menu.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

## ビデオリストの保存
ビデオリストは、リストファイルに保存し、後で必要に応じて読み込むことができます。

リストに1つ以上のビデオが含まれている場合、☰アイコンをクリックし、`ビデオリストの保存...`を選択します。ダイアログが表示され、保存するディレクトリとファイル名を変更できます。

## ビデオリストの読み込み
毎回ビデオを追加する代わりに、以前に保存したビデオリストを読み込むことができます。

☰アイコンをクリックし、`ビデオリストの読み込み...`を選択します。ダイアログが表示され、ビデオリストファイルを選択できます。

読み込んだリストにあるビデオが現在のリストに既に存在する場合、それが自動的に認識され、適切に処理されます。

## リストの更新
リストをすぐに更新するには、☰アイコンをクリックし、`更新`を選択します。

## Chzzk Downloader Suiteの環境を開く
Chzzk Downloader Suiteの環境を開くには、☰アイコンをクリックし、`ダウンローダー`の下にある`環境（Command Prompt）`または`環境（PowerShell）`を選択します。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_environment.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

## 保存ディレクトリを開く
ダウンロードしたビデオの保存ディレクトリを開くには、☰アイコンをクリックし、`ダウンローダー`の下にある`保存ディレクトリを開く`を選択します。

## Chzzk Video Downloaderの設定の表示
Chzzk Video Downloaderの設定を表示するには、☰アイコンをクリックし、`ダウンローダー`の下にある`設定を表示...`を選択します。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_configuration.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

## 最小化時にトレイに移動
`機能`設定で`最小化時にトレイに移動`オプションが有効になっている場合、Chzzk Video Managerが最小化されるとシステムトレイに移動します。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_tray_icon.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

トレイのアイコンをダブルクリックするとウィンドウが元の状態に戻り、トレイのアイコンを右クリックすると、以下の画像のようなメニューが表示されます。

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_tray_menu.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

## その他の設定

### 起動

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_settings_startup.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

* **起動時にウィンドウのサイズと位置を記憶** - 終了時にウィンドウのサイズと位置を保存し、次回起動時に復元します。
* **起動時にChzzk Video Managerの最新アップデートを確認** - 起動時にChzzk Video Managerの最新アップデートを確認するかどうかを設定します。手動で確認する場合は、`アップデート確認`ボタンをクリックします。

### 機能

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_settings_features.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

* **更新間隔 (秒)** - リストの画面更新間隔を設定します。
* **パフォーマンスレベル** - Chzzk Video Managerが現在実行されているシステムのパフォーマンスを指定します。ビデオの追加や更新時にタイムアウトによるエラーが発生する場合、パフォーマンスレベルを1段階下げて再試行してください。

### ダウンローダー

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_settings_downloader.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

* **JSON-RPCサーバー: ホストアドレス** - JSON-RPCサーバーのホストアドレスを設定します。
* **JSON-RPCサーバー: ポート** - JSON-RPCサーバーのポート番号を設定します。
* **JSON-RPCサーバー: ID** - JSON-RPCサーバーのIDを設定します。
* **サムネイル画像を保存** - サムネイル画像を別途保存するかどうかを設定します。
* **目標画質** - ダウンロードする際の画質を設定します。

### 認証

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_settings_auth.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

* **認証キー (NID_AUT)** - * NAVER IDの認証キーを指定します。
* **セッションキー (NID_SES)** - NAVER IDのセッションキーを指定します。

Chzzk認証資格情報の取得方法については、`how_to_get_chzzk_credential.ja-JP.pdf`を参照してください。

### ディレクトリ

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_settings_directory.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

* **作業ディレクトリ** - Chzzk Video Downloaderの設定ファイルが保存されるディレクトリを指定します。
* **保存ディレクトリ** - ダウンロードしたビデオファイルが保存されるディレクトリを指定します。
* **一時ディレクトリ** - 一時ファイルが作成されるディレクトリを指定します。

### バージョン情報

<div style='text-align: center'>
<img src='../../img/screenshots/vman_ja-JP/vman_settings_about.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

* **バージョン情報** - Chzzk Video Managerのバージョン情報を表示します。
* **お問い合わせリンク** - 作成者への連絡先リンクです。

## お問い合わせ
Chzzk Downloader Suiteに関するご質問、バグ報告、または改善要望がございましたら、[GitHub](https://github.com/Choonholic/ChzzkDownloader/)の[Issues](https://github.com/Choonholic/ChzzkDownloader/issues/new)機能を通じてお知らせください。全ての言語に対応可能ですが、直接対応可能な言語は韓国語、英語、日本語、中国語です。他の言語については、機械翻訳を通じて対応するため、100%正確に対応できない場合があります。