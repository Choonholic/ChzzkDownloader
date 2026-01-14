# Chzzk Transport Finalizer
Chzzkのストリーム用の最終処理ツール

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_chzzktransportfinalizer.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

## バージョン
Version 1.36.0, January 15, 2026 00:00:00

## 必須事項
* **[必須]** FFmpegの公式メジャーバージョン（FFmpeg 7.0またはそれ以上が必要）

## 使用法
```
ChzzkTransportFinalizer
  [-h] [--version] [-d [DISPLAY]] [--work [WORK]]
  [--work-user [WORK_USER]] [--work-pass [WORK_PASS]] [--watch [WATCH]]
  [--watch-trav [WATCH_TRAV]] [--watch-user [WATCH_USER]]
  [--watch-pass [WATCH_PASS]] [--exclude [EXCLUDE]]
  [--exclude-trav [EXCLUDE_TRAV]] [--exclude-user [EXCLUDE_USER]]
  [--exclude-pass [EXCLUDE_PASS]] [--convert [CONVERT]] [--ext [EXT]]
  [--exist [EXIST]] [--threshold [THRESHOLD]] [--rpc]
  [--rpcexpose [RPCEXPOSE]] [--rpcport [RPCPORT]] [--rpcid [RPCID]]
  [--snapshot SNAPSHOT] [--metadata [METADATA]] [--startup [STARTUP]]
  [--pnpath [PNPATH]] [--pnlanguage [PNLANGUAGE]] [--pnparams [PNPARAMS]]
  [--pntexttype [PNTEXTTYPE]] [--settings [SETTINGS]] [--reset]
```

## オプション
```
-h, --help                    このヘルプメッセージを表示
--version                     バージョン情報を表示
-d, --display [DISPLAY]       表示モードを設定（quiet|simple|fluent|all）
--work [WORK]                 作業ディレクトリを設定
--work-user [WORK_USER]       作業ディレクトリがリモートネットワーク上にある場合に使用するユーザー名を設定
--work-pass [WORK_PASS]       作業ディレクトリがリモートネットワーク上にある場合に使用するパスワードを設定
--watch [WATCH]               監視ディレクトリを設定
--watch-trav [WATCH_TRAV]     監視ディレクトリの探索方式を設定 (direct|recursive)
--watch-user [WATCH_USER]     監視ディレクトリがリモートネットワーク上にある場合に使用するユーザー名を設定
--watch-pass [WATCH_PASS]     監視ディレクトリがリモートネットワーク上にある場合に使用するパスワードを設定
--exclude [EXCLUDE]           監視除外ディレクトリを設定
--exclude-trav [EXCLUDE_TRAV] 除外ディレクトリの探索方式を設定 (direct|recursive)
--exclude-user [EXCLUDE_USER] 除外ディレクトリがリモートネットワーク上にある場合に使用するユーザー名を設定
--exclude-pass [EXCLUDE_PASS] 除外ディレクトリがリモートネットワーク上にある場合に使用するパスワードを設定
--convert [CONVERT]           変換パラメータを設定
--ext [EXT]                   保存ファイルの拡張子を設定
--exist [EXIST]               対象ファイルが既に存在する場合の保存方法を設定 (rename|skip|overwrite)
--threshold [THRESHOLD]       ディスク容量が不足している場合にダウンロードを停止するしきい値を、サイズまたはパーセント(%)で設定 (無効化: -, 既定値: 5%, 有効範囲: ディスク総容量の1～50%)
--rpc                         JSON-RPCサーバーを有効化
--rpcexpose [RPCEXPOSE]       JSON-RPCサーバーの公開方法を設定 (close|open)
--rpcport [RPCPORT]           JSON-RPCサーバーのポートを設定 （デフォルト: 65000, 49152-65300）
--rpcid [RPCID]               JSON-RPCサーバーのIDを設定 （デフォルト: 70）
--snapshot SNAPSHOT           ステータスが変更されるたびにJSONファイルにスナップショットを保存
--metadata [METADATA]         メタデータを保存またはスキップ（save|skip）
--startup [STARTUP]           起動方法を設定（normal|fast）
--pnpath [PNPATH]             通知プラグインのパスを設定
--pnlanguage [PNLANGUAGE]     通知プラグインで使用する言語を設定
--pnparams [PNPARAMS]         通知プラグインのパラメーターを設定
--pntexttype [PNTEXTTYPE]     通知プラグインで使用するテキスト形式を設定 (plain|markdown|html)
--settings [SETTINGS]         設定保存時の動作を設定（default|skip|quit）
--reset                       すべての設定をリセット
```

## 使用例
```powershell
ChzzkTransportFinalizer --work work --watch out
```

## 説明
Chzzk Transport Finalizerは、Chzzk Live DownloaderとChzzk Video Downloaderが直接最終処理を行う代わりに、別のプロセスで順次最終処理を実行するよう設計されたツールです。Chzzk Transport Finalizerを使用することで、ライブストリームが短い間隔で放送される場合でも、影響を受けずにダウンロードできるように支援します。

## 作業ディレクトリの設定
作業に必要なファイルが保存されるディレクトリを指定するには、以下のコマンドを使用します。

```powershell
ChzzkTransportFinalizer --work work
```

このオプションをデフォルトに設定したい場合は、以下のように`--work`のみを使用してください。

```powershell
ChzzkTransportFinalizer --work
```

## 監視ディレクトリの設定
Chzzk Transport Finalizerはストリームファイルが保存されるディレクトリを監視し、新しいファイルが追加されると自動的に最終変換を実行します。監視するディレクトリを指定するには、次のコマンドを使用してください。

```powershell
ChzzkTransportFinalizer --watch out
```

このオプションをデフォルトに設定したい場合は、以下のように`--watch`のみを使用してください。

```powershell
ChzzkTransportFinalizer --watch
```

## 監視ディレクトリの探索方式の設定
Chzzk Transport Finalizerはディレクトリを監視する際、デフォルトでは指定したディレクトリとその配下のすべてのサブディレクトリを探索します。指定したディレクトリのみを監視したい場合は、次のコマンドを使用してください。

```powershell
ChzzkTransportFinalizer --watch out --watch-trav direct
```

このオプションをデフォルトの動作に戻したい場合は、探索方式を指定せずに`--watch-trav`のみを使用してください。

```powershell
ChzzkTransportFinalizer --watch out --watch-trav
```

## 監視除外ディレクトリの設定
Chzzk Transport Finalizerは、選択したオプションに応じて、監視ディレクトリ全体または最上位ディレクトリのみを監視します。次のコマンドを使用すると、監視ディレクトリのサブディレクトリや他のディレクトリを監視対象から除外することができます。

```powershell
ChzzkTransportFinalizer --watch out --exclude out\exc
```

監視除外ディレクトリの設定を解除したい場合は、ディレクトリを指定せずに`--exclude`のみを使用してください。

```powershell
ChzzkTransportFinalizer --watch out --exclude
```

## 除外ディレクトリの探索方式の設定
監視除外ディレクトリが指定されている場合、Chzzk Transport Finalizerはデフォルトでは指定したディレクトリのみを探索します。指定したディレクトリの配下にあるすべてのサブディレクトリも除外したい場合は、次のコマンドを使用してください。

```powershell
ChzzkTransportFinalizer --watch out --excluded out\exc --exclude-trav recursive
```

このオプションをデフォルトの動作に戻したい場合は、探索方式を指定せずに`--exclude-trav`のみを使用してください。

```powershell
ChzzkTransportFinalizer --watch out --excluded out\exc --exclude-trav
```

## ディレクトリ指定方法
`--work`、`--watch`、`--exclude` オプションでディレクトリを指定する場合、ディレクトリは次のように指定できます。

```powershell
ChzzkTransportFinalizer --work work
```

実行ファイルが存在するディレクトリのサブディレクトリである`work`ディレクトリを作業ディレクトリとして指定します。このディレクトリが存在しない場合は、新しく作成されます。

```powershell
ChzzkTransportFinalizer --watch \Users\Username\Documents\chzzk
```

現在のドライブ上の`\Users\Username\Documents\chzzk`ディレクトリを監視ディレクトリとして指定します。このディレクトリが存在しない場合は、新しく作成されます。

```powershell
ChzzkTransportFinalizer --watch C:\Users\Username\Documents\chzzk
```

もちろん、上記のようにドライブ(例:`C:`)を直接指定することもできます。

```powershell
ChzzkTransportFinalizer --watch \\192.168.0.1\chzzk
```

`\\192.168.0.1\chzzk`のUNCパスを基盤としたネットワークストレージのディレクトリを監視ディレクトリとして指定します。このディレクトリが存在しない場合は、新しく作成されます。

ネットワークストレージにファイルを保存する際、接続するためにユーザー名とパスワードを入力する必要があります。この情報は次のように指定できます。

```powershell
ChzzkTransportFinalizer --work-user username --work-pass password
ChzzkTransportFinalizer --watch-user username --watch-pass password
```

### 最終処理の変換パラメータの設定
`--convert`パラメータを使用して最終処理に使用するエンコードオプションを指定できます。エンコードオプション自体がコマンドライン引数の形式を取るため、エラーを防ぐには`=`演算子と`"`の引用符で囲む必要があります。例えば、次の設定は`HEVC`コーデックでエンコードするように指定しています:

```powershell
ChzzkTransportFinalizer --convert="-c:v libx265 -crf 25 -c:a aac -b:a 128k"
```

設定内容を変換パラメータセットファイルとして保存しておき、実行時にその内容を読み込んで処理することも可能です。

```text
-c:v libx265 -crf 25 -c:a aac -b:a 128k
```

たとえば、`hevc_sw_128k.set`というファイルに上記の内容が保存されている場合、以下のようにファイル名を指定できます。

```powershell
ChzzkTransportFinalizer --convert=hevc_sw_128k.set
```

このオプションをデフォルトに設定したい場合は、以下のように`--convert`のみを使用してください。

```powershell
ChzzkTransportFinalizer --convert
```

また、変換パラメータに応じて拡張子を変更する必要がある場合は、`--ext` パラメータで指定できます。

```powershell
ChzzkTransportFinalizer --convert=av1_nvenc_128k.set --ext=.av1
```

## メタデータの保存
ストリーム情報を基に動画にメタデータを保存するには、以下のコマンドを使用します。Chzzk Transport Finalizerは、Chzzk Live DownloaderまたはChzzk Video Downloaderによってトランスポートファイルと共に`JSON`形式で出力されたストリーム情報を使用します。このファイルが作成されていないか、削除されている場合、メタデータは保存されません。

```powershell
ChzzkTransportFinalizer --metadata save
```

この機能をオフにするには、以下のコマンドを使用します。

```powershell
ChzzkTransportFinalizer --metadata skip
```

## 表示モードの設定
デフォルトでは、詳細な情報が表示されます。ただし、情報が不要な場合は、以下のコマンドで非表示にすることができます。

```powershell
ChzzkTransportFinalizer -d quiet
ChzzkTransportFinalizer --display quiet
```

`--display`パラメータで設定可能な表示モードは以下の通りです。

* `quiet` - すべての情報を非表示にします。
* `simple` - 簡単な情報のみを表示します。
* `fluent` - 詳細な情報を表示します。
* `all` - すべての情報を表示します。

このオプションをデフォルトに設定したい場合は、以下のように`-d`または`--display`のみを使用してください。

```powershell
ChzzkTransportFinalizer -d
ChzzkTransportFinalizer --display
```

## 対象ファイルが既に存在する場合の保存方法の設定
デフォルトでは、同じ名前のファイルが既に存在する場合、ファイル名の後ろに`(n)`を付けて保存します。ただし、次のコマンドを使用してファイルを上書きするか、最終処理自体をスキップするよう設定できます。

```powershell
ChzzkTransportFinalizer --exist overwrite
ChzzkTransportFinalizer --exist skip
```

このオプションをデフォルトに設定したい場合は、以下のように`--exist`のみを使用してください。

```powershell
ChzzkTransportFinalizer --exist
```

## 空き容量が閾値を下回った場合に最終処理を停止する設定
デフォルトでは、保存ディレクトリおよび一時ディレクトリの空き容量が5%以下になると、最終処理を停止します。空き容量のしきい値を変更するには、次のコマンドを使用してください。しきい値はサイズまたはパーセント(%)で指定でき、有効範囲はディスク総容量の 1～50%です。

```powershell
ChzzkTransportFinalizer --threshold 20%
ChzzkTransportFinalizer --threshold 1GB
ChzzkTransportFinalizer --threshold 100M
ChzzkTransportFinalizer --threshold 800MiB
```

サイズでしきい値を指定する場合は、SI 単位（KB、MB、GB...）または IEC 単位（KiB、MiB、GiB...）を使用できます。また、接頭辞のみ（K、Ki、M、Mi、G、Gi...）を指定することも可能です。もちろん、単位を付けずにバイト単位で指定することもできます。

空き容量に応じた最終処理停止機能を無効化するには、以下のコマンドを使用してください。

```powershell
ChzzkTransportFinalizer --threshold -
```

このオプションをデフォルト値にリセットするには、引数なしで`--threshold`を使用してください。

```powershell
ChzzkTransportFinalizer --threshold
```

## 設定保存時の動作設定
すべてのオプションは、デフォルトで設定ファイルに自動保存されます。

ただし、`--settings`パラメーターの後にオプションを指定することで、設定を保存するかどうか、または設定内容を確認するかを選択できます。

```powershell
ChzzkTransportFinalizer --settings skip
```

* `default` – 選択したオプションを設定ファイルに保存してから、最終処理を進めます。
* `skip` – 選択したオプションを保存せず、現在のセッションにのみ適用してから、最終処理を進めます。
* `update` – 選択したオプションを設定ファイルに保存し、変更された設定内容を表示して終了します。
* `show` – 選択したオプションをすべて無視し、既存の設定内容を表示して終了します。
* `quit` – 選択したオプションを設定ファイルに保存して終了します。

## 設定保存時の動作を設定
すべてのオプションはデフォルトで設定ファイルに保存されますが、現在のセッションにのみ適用し、保存しない場合は以下のコマンドを使用してください。

```powershell
ChzzkTransportFinalizer --settings skip
```

最終処理せずに設定を保存して終了したい場合は、以下のコマンドを使用してください。

```powershell
ChzzkTransportFinalizer --settings quit
```

## プラグイン
Chzzk Transport Finalizerは、プラグインを通じてユーザーの個人の嗜好や環境に合わせた追加機能を提供します。

### 通知プラグイン
通知プラグインを登録すると、Chzzk Transport Finalizerの動作状態を外部ソリューションを通じて簡単に確認できます。デフォルトで提供する通知プラグインは次の通りです。

* `pn_slack` - Slack通知プラグイン
* `pn_telegram` - Telegram通知プラグイン

次のように`--pnpath`パラメータを使用することで通知プラグインを登録できます。通知プラグインは一度に一つのみ有効となるため、複数回登録した場合は最後に登録されたプラグインのみが有効になります。プラグインが登録されると、以降に起動されるすべてのChzzk Transport Finalizerに適用されます。

```powershell
ChzzkTransportFinalizer --pnpath=pn_...
```

`--pnlanguage`パラメータを使用して通知メッセージの言語を指定できます。

```powershell
ChzzkTransportFinalizer --pnpath=pn_... --pnlanguage=ko-KR
```

通知プラグインがMarkdown形式またはHTML形式をサポートしている場合は、`--pntexttype`パラメータを使用して通知メッセージのテキスト形式を指定できます。

```powershell
ChzzkTransportFinalizer --pnpath=pn_... --pntexttype=html
```

通知プラグインにはユーザーが独自に開発したプラグインも指定することができ、その際にプラグインに渡す必要があるパラメータがある場合は、`--pnparams`パラメータを使用して指定できます。このときメッセージが入る位置には`%M`を指定する必要があります。

```powershell
ChzzkTransportFinalizer --pnpath=userpn_... --pnparams="--user --message %M"
```

通知プラグインの登録を解除するには、プラグインを指定せずに`--pnpath`のみを使用してください。

```powershell
ChzzkTransportFinalizer --pnpath
```

## すべての設定をリセット
長期使用の間に設定が複雑になった場合、すべての設定をリセットするには以下のコマンドを使用してください。

```powershell
ChzzkTransportFinalizer --reset
```

これにより、以下の情報がリセットされます。

* プロセス詳細の表示設定
* 監視ディレクトリの設定
* 変換パラメータの設定

## バージョン情報の表示
バージョン情報を確認するには、以下のコマンドを使用します。

```powershell
ChzzkTransportFinalizer --version
```

## ヘルプの表示
簡単なパラメータヘルプを表示するには、以下のコマンドを使用します。

```powershell
ChzzkTransportFinalizer -h
ChzzkTransportFinalizer --help
```

## パラメータの優先順位
`--reset`、`-h`、`--version`以外のパラメータは、以下のように任意の順序で使用できますが、同じパラメータを複数使用することはできません。

```powershell
ChzzkTransportFinalizer -d quiet --watch out
```

`-h`および`--version`パラメータは、最初に使用されたもののみが処理され、その後すぐに終了します。したがって、以下のコマンドはバージョン情報のみを出力します。

```powershell
ChzzkTransportFinalizer --version -h
```

`--reset`パラメータは設定をリセットし、以前に設定された値を無視して終了します。したがって、以下のコマンドではビデオ番号が無視されます。

```powershell
ChzzkTransportFinalizer --watch out --reset
```

## JSON-RPCを使用した外部からの制御
詳細な情報については、`how_to_control_chzzk_transport_finalizer.ja-JP.pdf` をご参照ください。

## お問い合わせ
Chzzk Downloader Suiteに関するご質問、バグ報告、または改善要望がございましたら、[GitHub]（https://github.com/Choonholic/ChzzkDownloader/）の[Issues]（https://github.com/Choonholic/ChzzkDownloader/issues/new）機能を通じてお知らせください。全ての言語に対応可能ですが、直接対応可能な言語は韓国語、英語、日本語、中国語です。他の言語については、機械翻訳を通じて対応するため、100%正確に対応できない場合があります。
