# Chzzk Live Finalizer
Chzzkのストリーム用の最終処理ツール

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_chzzklivefinalizer.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

## バージョン
Version 1.5.2, December 30, 2024 00:00:00

## 使用法
```powershell
ChzzkLiveFinalizer [-h] [--version] [-d [DISPLAY]] [--work [WORK]] [--work-user [WORK_USER]]
                   [--work-pass [WORK_PASS]] [--watch [WATCH]] [--watch-user [WATCH_USER]]
                   [--watch-pass [WATCH_PASS]] [--convert [CONVERT]] [--exist [EXIST]]
                   [--threshold [THRESHOLD]] [--rpcid [RPCID]] [--rpcport [RPCPORT]]
                   [--snapshot SNAPSHOT] [--startup [STARTUP]] [--settings [SETTINGS]] [--reset]
```

## オプション
```
-h, --help               このヘルプメッセージを表示
--version                バージョン情報を表示
-d, --display [DISPLAY]  プロセスステータス表示モードを設定 (quiet|simple|fluent|all)
--work [WORK]            作業ディレクトリを設定
--work-user [WORK_USER]  作業ディレクトリがリモートネットワーク上にある場合に使用するユーザー名を設定
--work-pass [WORK_PASS]  作業ディレクトリがリモートネットワーク上にある場合に使用するパスワードを設定
--watch [WATCH]          監視ディレクトリを設定
--watch-user [WORK_USER] 監視ディレクトリがリモートネットワーク上にある場合に使用するユーザー名を設定
--watch-pass [WORK_PASS] 監視ディレクトリがリモートネットワーク上にある場合に使用するパスワードを設定
--convert [CONVERT]      変換パラメータを設定
--exist [EXIST]          対象ファイルが既に存在する場合の保存方法を設定 (rename|skip|overwrite)
--threshold [THRESHOLD]  空き容量が少ない場合に停止する閾値(%)を設定 (無効化: -, デフォルト: 10, 3-30)
--rpcid [RPCID]          JSON-RPCサーバーのIDを設定 （デフォルト: 70）
--rpcport [RPCPORT]      JSON-RPCサーバーのポートを設定 （デフォルト: 65000, 49152-65300）
--snapshot SNAPSHOT      ステータスが変更されるたびにJSONファイルにスナップショットを保存
--startup [STARTUP]      起動方法を設定（normal|fast）
--settings [SETTINGS]    設定保存時の動作を設定（default|skip|quit）
--reset                  すべての設定をリセット
```

## 使用例
```powershell
ChzzkLiveFinalizer --work work --watch out
```

## 説明
Chzzk Live Finalizerは、Chzzk Live Downloaderが直接最終処理を行う代わりに、別のプロセスで順次最終処理を実行するよう設計されたツールです。Chzzk Live Finalizerを使用することで、ライブストリームが短い間隔で放送される場合でも、影響を受けずにダウンロードできるように支援します。

## 作業ディレクトリの設定
作業に必要なファイルが保存されるディレクトリを指定するには、以下のコマンドを使用します。

```powershell
ChzzkLiveFinalizer --work work
```

このオプションをデフォルトに設定したい場合は、以下のように`--work`のみを使用してください。

```powershell
ChzzkLiveFinalizer --work
```

## 監視ディレクトリの設定
Chzzk Live Finalizerはストリームファイルが保存されるディレクトリを監視し、新しいファイルが追加されると自動的に最終変換を実行します。監視するディレクトリを指定するには、次のコマンドを使用してください。

```powershell
ChzzkLiveFinalizer --watch out
```

このオプションをデフォルトに設定したい場合は、以下のように`--watch`のみを使用してください。

```powershell
ChzzkLiveFinalizer --watch
```

## ディレクトリ指定方法
ディレクトリは次のように指定できます。

```powershell
ChzzkLiveFinalizer --work work
```

実行ファイルが存在するディレクトリのサブディレクトリである`work`ディレクトリを作業ディレクトリとして指定します。このディレクトリが存在しない場合は、新しく作成されます。

```powershell
ChzzkLiveFinalizer --watch \Users\Username\Documents\chzzk
```

現在のドライブ上の`\Users\Username\Documents\chzzk`ディレクトリを監視ディレクトリとして指定します。このディレクトリが存在しない場合は、新しく作成されます。

```powershell
ChzzkLiveFinalizer --watch C:\Users\Username\Documents\chzzk
```

もちろん、上記のようにドライブ(例:`C:`)を直接指定することもできます。

```powershell
ChzzkLiveFinalizer --watch \\192.168.0.1\chzzk
```

`\\192.168.0.1\chzzk`のUNCパスを基盤としたネットワークストレージのディレクトリを監視ディレクトリとして指定します。このディレクトリが存在しない場合は、新しく作成されます。

ネットワークストレージにファイルを保存する際、接続するためにユーザー名とパスワードを入力する必要があります。この情報は次のように指定できます。

```powershell
ChzzkLiveFinalizer --work-user username --work-pass password
ChzzkLiveFinalizer --watch-user username --watch-pass password
```

### 最終処理の変換パラメータの設定
`--convert`オプションで、最終処理中に変換パラメータを設定できます。例えば、以下のオプションで`FFmpeg`を使用して`H.265`コーデックでエンコードできます。

```powershell
ChzzkLiveFinalizer --convert "-c:v libx265 -preset medium -crf 23 -c:a aac -b:a 128k"
```

このオプションをデフォルトに設定したい場合は、以下のように`--convert`のみを使用してください。

```powershell
ChzzkLiveFinalizer --convert
```

## プロセス詳細の表示方法を設定
デフォルトでは、詳細なプロセス情報が表示されます。ただし、詳細が不要な場合は、以下のコマンドで表示を抑制できます。

```powershell
ChzzkLiveFinalizer -d quiet
ChzzkLiveFinalizer --display quiet
```

`--display`パラメータで設定可能な表示方法は以下の通りです。

* `quiet` - すべてのプロセス詳細を非表示にします。
* `fluent` - 詳細なプロセス情報をすべて表示します。
* `default` - `fluent`と同じです。

このオプションをデフォルトに設定したい場合は、以下のように`-d`または`--display`のみを使用してください。

```powershell
ChzzkLiveFinalizer -d
ChzzkLiveFinalizer --display
```

## 対象ファイルが既に存在する場合の保存方法の設定
デフォルトでは、同じ名前のファイルが既に存在する場合、ファイル名の後ろに`(n)`を付けて保存します。ただし、次のコマンドを使用してファイルを上書きするか、最終処理自体をスキップするよう設定できます。

```powershell
ChzzkLiveFinalizer --exist overwrite
ChzzkLiveFinalizer --exist skip
```

このオプションをデフォルトに設定したい場合は、以下のように`--exist`のみを使用してください。

```powershell
ChzzkLiveFinalizer --exist
```

## 空き容量が閾値を下回った場合に最終処理を停止する設定
デフォルトでは、保存ディレクトリまたは一時ディレクトリの空き容量が10%を下回ると、最終処理を停止します。空き容量の閾値を設定するには、以下のコマンドを使用してください。設定可能な値の範囲は`3`から`30`です。

```powershell
ChzzkLiveFinalizer --threshold 20
```

空き容量に応じた最終処理停止機能を無効化するには、以下のコマンドを使用してください。

```powershell
ChzzkLiveFinalizer --threshold -
```

このオプションをデフォルト値にリセットするには、引数なしで`--threshold`を使用してください。

```powershell
ChzzkLiveFinalizer --threshold
```

## 設定保存時の動作を設定
すべてのオプションはデフォルトで設定ファイルに保存されますが、現在のセッションにのみ適用し、保存しない場合は以下のコマンドを使用してください。

```powershell
ChzzkLiveFinalizer --settings skip
```

最終処理せずに設定を保存して終了したい場合は、以下のコマンドを使用してください。

```powershell
ChzzkLiveFinalizer --settings quit
```

## すべての設定をリセット
長期使用の間に設定が複雑になった場合、すべての設定をリセットするには以下のコマンドを使用してください。

```powershell
ChzzkLiveFinalizer --reset
```

これにより、以下の情報がリセットされます。

* プロセス詳細の表示設定
* 監視ディレクトリの設定
* 変換パラメータの設定

## バージョン情報の表示
バージョン情報を確認するには、以下のコマンドを使用します。

```powershell
ChzzkLiveFinalizer --version
```

## ヘルプの表示
簡単なパラメータヘルプを表示するには、以下のコマンドを使用します。

```powershell
ChzzkLiveFinalizer -h
ChzzkLiveFinalizer --help
```

## パラメータの優先順位
`--reset`、`-h`、`--version`以外のパラメータは、以下のように任意の順序で使用できますが、同じパラメータを複数使用することはできません。

```powershell
ChzzkLiveFinalizer -d quiet --watch out
```

`-h`および`--version`パラメータは、最初に使用されたもののみが処理され、その後すぐに終了します。したがって、以下のコマンドはバージョン情報のみを出力します。

```powershell
ChzzkLiveFinalizer --version -h
```

`--reset`パラメータは設定をリセットし、以前に設定された値を無視して終了します。したがって、以下のコマンドではビデオ番号が無視されます。

```powershell
ChzzkLiveFinalizer --watch out --reset
```

## JSON-RPCを使用した外部からの制御
詳細な情報については、`how_to_control_chzzk_live_finalizer.ja-JP.pdf` をご参照ください。

## お問い合わせ
Chzzk Downloader Suiteに関するご質問、バグ報告、または改善要望がございましたら、[GitHub]（https://github.com/Choonholic/ChzzkDownloader/）の[Issues]（https://github.com/Choonholic/ChzzkDownloader/issues/new）機能を通じてお知らせください。全ての言語に対応可能ですが、直接対応可能な言語は韓国語、英語、日本語、中国語です。他の言語については、機械翻訳を通じて対応するため、100%正確に対応できない場合があります。