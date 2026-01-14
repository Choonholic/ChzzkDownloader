# Chzzk Clip Downloader
Chzzkのクリップ用のダウンローダー

<div style='text-align: center'>
<img src='../../img/screenshots/screenshot_chzzkclipdownloader.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

## バージョン
Version 1.36.0, January 15, 2026 00:00:00

## 使用法
```
ChzzkClipDownloader
  [-h] [--version] [-i INPUT] [-a [AUTH]] [--authaut AUTHAUT]
  [--authses AUTHSES] [--authcookie AUTHCOOKIE] [--adult [ADULT]] [-y]
  [-d [DISPLAY]] [--name [NAME]] [--work [WORK]] [--work-user [WORK_USER]]
  [--work-pass [WORK_PASS]] [--out [OUT]] [--out-user [OUT_USER]]
  [--out-pass [OUT_PASS]] [--temp [TEMP]] [--temp-user [TEMP_USER]]
  [--temp-pass [TEMP_PASS]] [--category [CATEGORY]] [--exist [EXIST]]
  [--threshold [THRESHOLD]] [--rpc] [--rpcexpose [RPCEXPOSE]]
  [--rpcport [RPCPORT]] [--rpcid [RPCID]] [--snapshot SNAPSHOT]
  [--download [DOWNLOAD]] [--limit [LIMIT]] [--thumb [THUMB]]
  [--metadata [METADATA]] [--startup [STARTUP]] [--pnpath [PNPATH]]
  [--pnlanguage [PNLANGUAGE]] [--pnparams [PNPARAMS]]
  [--pntexttype [PNTEXTTYPE]] [--settings [SETTINGS]] [--reset]
  [clip]
```

### 位置引数
```
clip                      ダウンロードするクリップUIDまたはURL
```

### オプション
```
-h, --help                このヘルプメッセージを表示
--version                 バージョン情報を表示
-i, --input INPUT         ダウンロードリストファイルを設定
-a, --auth [AUTH]         Chzzk認証資格情報の処理方法を設定 (reuse|reissue|ignore)
--authaut AUTHAUT         Chzzk認証資格情報の認証キーを設定
--authses AUTHSES         Chzzk認証資格情報のセッションキーを設定
--authcookie AUTHCOOKIE   Chzzk認証資格情報を取得するためのNetscape形式のクッキーファイルを設定
--adult [ADULT]           認証情報が無効な場合のアダルトコンテンツ処理方法を設定（ask|skip）
-y, --yes                 すべての確認値を自動的に「はい」に設定
-d, --display [DISPLAY]   表示モードを設定（quiet|simple|fluent|all）
--info INFO               ダウンロードせずにクリップ情報を取得
--name [NAME]             保存ファイル名の形式を設定
--work [WORK]             作業ディレクトリを設定
--work-user [WORK_USER]   作業ディレクトリがリモートネットワーク上にある場合に使用するユーザー名を設定
--work-pass [WORK_PASS]   作業ディレクトリがリモートネットワーク上にある場合に使用するパスワードを設定
--out [OUT]               保存ディレクトリを設定
--out-user [OUT_USER]     保存ディレクトリがリモートネットワーク上にある場合に使用するユーザー名を設定
--out-pass [OUT_PASS]     保存ディレクトリがリモートネットワーク上にある場合に使用するパスワードを設定
--temp [TEMP]             一時ディレクトリを設定
--temp-user [TEMP_USER]   一時ディレクトリがリモートネットワーク上にある場合に使用するユーザー名を設定
--temp-pass [TEMP_PASS]   一時ディレクトリがリモートネットワーク上にある場合に使用するパスワードを設定
--category [CATEGORY]     保存時のカテゴリ分け方法を設定 (none|streamer)
--exist [EXIST]           対象ファイルが既に存在する場合の保存方法を設定 (rename|skip|overwrite)
--threshold [THRESHOLD]   ディスク容量が不足している場合にダウンロードを停止するしきい値を、サイズまたはパーセント(%)で設定 (無効化: -, 既定値: 5%, 有効範囲: ディスク総容量の1～50%)
--rpc                     JSON-RPCサーバーを有効化
--rpcexpose [RPCEXPOSE]   JSON-RPCサーバーの公開方法を設定 (close|open)
--rpcport [RPCPORT]       JSON-RPCサーバーのポートを設定（デフォルト: 64000, 49152-65300）
--rpcid [RPCID]           JSON-RPCサーバーのIDを設定（デフォルト: 50）
--snapshot SNAPSHOT       ステータスが変更されるたびにJSONファイルにスナップショットを保存
--download [DOWNLOAD]     ダウンロード方法を設定（default|atxc|alter）
--limit [LIMIT]           最大ダウンロード速度を設定 (例: 512K, 10M, 1G, デフォルト: 0)
--thumb [THUMB]           サムネイル画像を保存またはスキップ（save|skip）
--metadata [METADATA]     メタデータを保存またはスキップ（save|skip）
--startup [STARTUP]       起動方法を設定（normal|fast）
--pnpath [PNPATH]         通知プラグインのパスを設定
--pnlanguage [PNLANGUAGE] 通知プラグインで使用する言語を設定
--pnparams [PNPARAMS]     通知プラグインのパラメーターを設定
--pntexttype [PNTEXTTYPE] 通知プラグインで使用するテキスト形式を設定 (plain|markdown|html)
--settings [SETTINGS]     設定保存時の動作を設定（default|skip|quit）
--reset                   すべての設定をリセット
```

### 使用例
```powershell
ChzzkClipDownloader C46IcpG11p --thumb save --work work --out out --temp temp
```

## ダウンロードするクリップの設定
クリップUIDまたはURLを直接指定してクリップをダウンロードできます。

例えば、クリップのURLがhttps://chzzk.naver.com/clips/C46IcpG11pの場合、クリップUIDは**C46IcpG11p**です。このクリップをダウンロードするには、以下のコマンドを使用します。

```powershell
ChzzkClipDownloader C46IcpG11p
ChzzkClipDownloader https://chzzk.naver.com/clips/C46IcpG11p
```

複数のクリップを順番にダウンロードしたい場合は、以下のようにリストファイルを作成し、UTF-8形式のテキストファイルとして保存してください。（例: `list.txt`）

```python
# リストサンプル
https://chzzk.naver.com/clips/YY9plBpybL
C46IcpG11p
https://chzzk.naver.com/clips/gTSq4c8HaQ
https://chzzk.naver.com/clips/nZbWU27D95
```

その後、以下のコマンドを使用してダウンロードします。

```powershell
ChzzkClipDownloader -i list.txt
ChzzkClipDownloader --input list.txt
```

## 認証資格情報のリセット
成人限定クリップなど、NAVER認証資格情報が必要なクリップをダウンロードするには、以下の情報を指定する必要があります。

* Chzzkのクッキーから取得したNAVER IDの認証キー（`NID_AUT`）
* Chzzkのクッキーから取得したNAVER IDのセッションキー（`NID_SES`）

認証資格情報が必要なクリップをダウンロードする際に、認証資格情報が見つからない場合は、認証情報の入力プロンプトが自動的に表示されます。

一度入力すると、デフォルトとして設定され、以後の実行では再入力の必要はありません。Chzzk認証資格情報の取得方法については、`how_to_get_chzzk_credential.ja-JP.pdf`を参照してください。

認証資格情報が変更された場合や、別のIDでログインしてリセットする必要がある場合は、以下のコマンドを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url -a reset
ChzzkClipDownloader clip_uid または url --auth reset
```

一時的に認証情報を無視する必要がある場合は、以下のコマンドを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url -a ignore
ChzzkClipDownloader clip_uid または url --auth ignore
```

`-y`または`--yes`パラメータを使用すると、確認なしで認証情報の入力プロンプトが自動的に表示されます。

```powershell
ChzzkClipDownloader clip_uid または url -y
ChzzkClipDownloader clip_uid または url --yes
```

## 保存ファイル名の形式設定
デフォルトでは、保存されるクリップとサムネイルのファイル名は`[{download_date}][{name}] {title}`の形式になります。この形式を変更したい場合は、以下のコマンドを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url --name "[{name}][{category}] {title}"
```

このオプションをデフォルトに設定したい場合は、以下のように`--name`のみを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url --name
```

### ファイル名形式タグ
ファイル名形式には以下の定義済みタグを使用できます。

* `{name}` - チャンネル名。
* `{verified}` - チャンネルが認証済みの場合、このタグは`[✓]`になります（認証されていない場合は空）。
* `{clip_uid}` - クリップUID。
* `{title}` - クリップのタイトル。
* `{download_date...}` - ストリーム開始時の日付関連タグ。
* `{media...}` - メディア情報関連のタグ。

メディア関連タグでは以下の要素が利用できます。

* `{media_quality}` - メディア品質（例: `1080p`）。
* `{media_video_width}` - ビデオの幅（ピクセル, 例: `1920`）。
* `{media_video_height}` - ビデオの高さ（ピクセル, 例: `1080`）。
* `{media_video_bitrate}` - ビデオビットレート（ビット/秒, 例: `8000000`）。
* `{media_audio_bitrate}` - オーディオビットレート（ビット/秒, 例: `192000`）。
* `{media_video_codec}` - ビデオコーデック（例: `H264`）。

日付関連タグでは、以下の詳細要素を展開できます。

* `{..._date}` - 日付（`%Y%m%d%H%M%S` 形式, 例: `20240607014327`）。
* `{..._date_year}` または `{..._date_year_full}` - 世紀を含む年（例: `2024`）。
* `{..._date_year_short}` - 世紀を含まない年（ゼロ埋め形式, 例: `24`）。
* `{..._date_month}` - 月（ゼロ埋め形式, `01`, `02`, ..., `12`）。
* `{..._date_month_full}` - 月の完全な名称（`January`, `February`, ..., `December`）。
* `{..._date_month_short}` - 月の略称（`Jan`, `Feb`, ..., `Dec`）。
* `{..._date_day}` - 日（ゼロ埋め形式, `01`, `02`, ..., `31`）。
* `{..._date_hour}` - 時（24時間表記, ゼロ埋め形式, `00`, `01`, ..., `23`）。
* `{..._date_minute}` - 分（ゼロ埋め形式, `00`, `01`, ..., `59`）。
* `{..._date_second}` - 秒（ゼロ埋め形式, `00`, `01`, ..., `59`）。

## サムネイル画像の保存
サムネイル画像を別途保存するには、以下のコマンドを使用します。

```powershell
ChzzkClipDownloader clip_uid または url --thumb save
```

この機能をオフにするには、以下のコマンドを使用します。

```powershell
ChzzkClipDownloader clip_uid または url --thumb skip
```

## メタデータの保存
クリップ情報を基に動画にメタデータを保存するには、以下のコマンドを使用します。

```powershell
ChzzkClipDownloader clip_uid または url --metadata save
```

この機能をオフにするには、以下のコマンドを使用します。

```powershell
ChzzkClipDownloader clip_uid または url --metadata skip
```

## 表示モードの設定
デフォルトでは、詳細な情報が表示されます。ただし、情報が不要な場合は、以下のコマンドで非表示にすることができます。

```powershell
ChzzkClipDownloader clip_uid または url -d quiet
ChzzkClipDownloader clip_uid または url --display quiet
```

`--display`パラメータで設定可能な表示モードは以下の通りです。

* `quiet` - すべての情報を非表示にします。
* `simple` - 簡単な情報のみを表示します。
* `fluent` - 詳細な情報を表示します。
* `all` - すべての情報を表示します。

このオプションをデフォルトに設定したい場合は、以下のように`-d`または`--display`のみを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url -d
ChzzkClipDownloader clip_uid または url --display
```

## 作業ディレクトリの設定
作業に必要なファイルが保存されるディレクトリを指定するには、以下のコマンドを使用します。

```powershell
ChzzkClipDownloader clip_uid または url --work work
```

このオプションをデフォルトに設定したい場合は、以下のように`--work`のみを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url --work
```

## 保存ディレクトリの設定
ダウンロードしたファイルが保存されるディレクトリを指定するには、以下のコマンドを使用します。

```powershell
ChzzkClipDownloader clip_uid または url --out out
```

デフォルトでは、すべてのファイルはストリーマーごとのサブディレクトリに分類して保存されます。ストリーマーごとに分類せずに保存する場合は、次のコマンドを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url --category none
```

このオプションをデフォルトに設定したい場合は、以下のように`--out`または`--category`のみを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url --out --category
```

## 一時ディレクトリの設定
ダウンロード中のファイルが保存される一時ディレクトリを指定するには、以下のコマンドを使用します。

```powershell
ChzzkClipDownloader clip_uid または url --temp temp
```

このオプションをデフォルトに設定したい場合は、以下のように`--temp`のみを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url --temp
```

## ディレクトリ指定方法
ディレクトリは次のように指定できます。

```powershell
ChzzkClipDownloader clip_uid or url --temp temp
```

実行ファイルが存在するディレクトリのサブディレクトリである`temp`ディレクトリを一時ディレクトリとして指定します。このディレクトリが存在しない場合は、新しく作成されます。

```powershell
ChzzkClipDownloader clip_uid or url --work \Users\Username\Documents\chzzk_work
```

現在のドライブ上の`\Users\Username\Documents\chzzk_work`ディレクトリを作業ディレクトリとして指定します。このディレクトリが存在しない場合は、新しく作成されます。

```powershell
ChzzkClipDownloader clip_uid or url --work C:\Users\Username\Documents\chzzk_work
```

もちろん、上記のようにドライブ(例:`C:`)を直接指定することもできます。

```powershell
ChzzkClipDownloader clip_uid or url --out \\192.168.0.1\chzzk\out
```

`\\192.168.0.1\chzzk\out`のUNCパスを基盤としたネットワークストレージのディレクトリを保存ディレクトリとして指定します。このディレクトリが存在しない場合は、新しく作成されます。

ネットワークストレージにファイルを保存する際、接続するためにユーザー名とパスワードを入力する必要があります。この情報は次のように指定できます。

```powershell
ChzzkClipDownloader clip_uid or url --work-user username --work-pass password
ChzzkClipDownloader clip_uid or url --out-user username --out-pass password
ChzzkClipDownloader clip_uid or url --temp-user username --temp-pass password
```

## 対象ファイルが既に存在する場合の保存方法の設定
デフォルトでは、同じ名前のファイルが既に存在する場合、ファイル名の後ろに`(n)`を付けて保存します。ただし、次のコマンドを使用してファイルを上書きするか、ダウンロード自体をスキップするよう設定できます。

```powershell
ChzzkClipDownloader clip_uid または url --exist overwrite
ChzzkClipDownloader clip_uid または url --exist skip
```

このオプションをデフォルトに設定したい場合は、以下のように`--exist`のみを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url --exist
```

## 最大ダウンロード速度の設定 (ネットワーク帯域幅の制御)
ネットワーク帯域幅を制御するためにダウンロード速度を制限する必要がある場合は、以下のコマンドを使用してください。`0`を指定すると制限なしになります。`K`、`M`、`G`を付加できます。(`1K` = `1024`, `1M` = `1024K`, `1G` = `1024M`)

```powershell
ChzzkClipDownloader clip_uid or または --limit 10M
```

このオプションをデフォルトに設定したい場合は、以下のように`--limit`のみを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url --limit
```

## 空き容量が閾値を下回った場合にダウンロードを停止する設定
デフォルトでは、保存ディレクトリおよび一時ディレクトリの空き容量が5%以下になると、ダウンロードを停止します。空き容量のしきい値を変更するには、次のコマンドを使用してください。しきい値はサイズまたはパーセント(%)で指定でき、有効範囲はディスク総容量の 1～50%です。

```powershell
ChzzkClipDownloader clip_uid または url --threshold 20%
ChzzkClipDownloader clip_uid または url --threshold 1GB
ChzzkClipDownloader clip_uid または url --threshold 100M
ChzzkClipDownloader clip_uid または url --threshold 800MiB
```

サイズでしきい値を指定する場合は、SI 単位（KB、MB、GB...）または IEC 単位（KiB、MiB、GiB...）を使用できます。また、接頭辞のみ（K、Ki、M、Mi、G、Gi...）を指定することも可能です。もちろん、単位を付けずにバイト単位で指定することもできます。

空き容量に応じたダウンロード停止機能を無効化するには、以下のコマンドを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url --threshold -
```

このオプションをデフォルト値にリセットするには、引数なしで --threshold を使用してください。

```powershell
ChzzkClipDownloader clip_uid または url --threshold
```

## ダウンロード方法の設定
軽量なダウンロードモジュールが代替として含まれています。代替モジュールを試すには、以下のコマンドを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url --download alter
```

## 設定保存時の動作設定
すべてのオプションは、デフォルトで設定ファイルに自動保存されます。

ただし、`--settings`パラメーターの後にオプションを指定することで、設定を保存するかどうか、または設定内容を確認するかを選択できます。

```powershell
ChzzkClipDownloader clip_uid または url --settings skip
```

* `default` – 選択したオプションを設定ファイルに保存してから、ダウンロードを進めます。
* `skip` – 選択したオプションを保存せず、現在のセッションにのみ適用してから、ダウンロードを進めます。
* `update` – 選択したオプションを設定ファイルに保存し、変更された設定内容を表示して終了します。
* `show` – 選択したオプションをすべて無視し、既存の設定内容を表示して終了します。
* `quit` – 選択したオプションを設定ファイルに保存して終了します。

なお、次の情報は別途管理されており、`--settings`パラメーターのオプションに関係なく常に保存されます。

* Chzzkのクッキーから取得したNAVER IDの認証キー（`NID_AUT`）
* Chzzkのクッキーから取得したNAVER IDのセッションキー（`NID_SES`）

## プラグイン
Chzzk Clip Downloaderは、プラグインを通じてユーザーの個人の嗜好や環境に合わせた追加機能を提供します。

### 通知プラグイン
通知プラグインを登録すると、Chzzk Clip Downloaderの動作状態を外部ソリューションを通じて簡単に確認できます。デフォルトで提供する通知プラグインは次の通りです。

* `pn_slack` - Slack通知プラグイン
* `pn_telegram` - Telegram通知プラグイン

次のように`--pnpath`パラメータを使用することで通知プラグインを登録できます。通知プラグインは一度に一つのみ有効となるため、複数回登録した場合は最後に登録されたプラグインのみが有効になります。プラグインが登録されると、以降に起動されるすべてのChzzk Clip Downloaderに適用されます。

```powershell
ChzzkClipDownloader clip_uid または url --pnpath=pn_...
```

`--pnlanguage`パラメータを使用して通知メッセージの言語を指定できます。

```powershell
ChzzkClipDownloader clip_uid または url --pnpath=pn_... --pnlanguage=ko-KR
```

通知プラグインがMarkdown形式またはHTML形式をサポートしている場合は、`--pntexttype`パラメータを使用して通知メッセージのテキスト形式を指定できます。

```powershell
ChzzkClipDownloader clip_uid または url --pnpath=pn_... --pntexttype=html
```

通知プラグインにはユーザーが独自に開発したプラグインも指定することができ、その際にプラグインに渡す必要があるパラメータがある場合は、`--pnparams`パラメータを使用して指定できます。このときメッセージが入る位置には`%M`を指定する必要があります。

```powershell
ChzzkClipDownloader clip_uid または url --pnpath=userpn_... --pnparams="--user --message %M"
```

通知プラグインの登録を解除するには、プラグインを指定せずに`--pnpath`のみを使用してください。

```powershell
ChzzkClipDownloader clip_uid または url --pnpath
```

## すべての設定をリセット
長期使用の間に設定が複雑になった場合、すべての設定をリセットするには以下のコマンドを使用してください。

```powershell
ChzzkClipDownloader --reset
```

これにより、以下の情報がリセットされます。

* Chzzkのクッキーから取得したNAVER IDの認証キー（`NID_AUT`）
* Chzzkのクッキーから取得したNAVER IDのセッションキー（`NID_SES`）
* サムネイル画像の保存設定
* ダウンロード詳細の表示設定
* 保存ディレクトリと一時ディレクトリの設定

## バージョン情報の表示
バージョン情報を確認するには、以下のコマンドを使用します。

```powershell
ChzzkClipDownloader --version
```

## ヘルプの表示
簡単なパラメータヘルプを表示するには、以下のコマンドを使用します。

```powershell
ChzzkClipDownloader -h
ChzzkClipDownloader --help
```

## パラメータの優先順位
`--reset`、`-h`、`--version`以外のパラメータは、以下のように任意の順序で使用できますが、同じパラメータを複数使用することはできません。

```powershell
ChzzkClipDownloader C46IcpG11p --out out
```

`-h`および`--version`パラメータは、最初に使用されたもののみが処理され、その後すぐに終了します。したがって、以下のコマンドはバージョン情報のみを出力します。

```powershell
ChzzkClipDownloader --version -h
```

`--reset`パラメータは設定をリセットし、以前に設定された値を無視して終了します。したがって、以下のコマンドではクリップUIDが無視されます。

```powershell
ChzzkClipDownloader C46IcpG11p --reset
```

## 推奨初期設定
初回使用時には、以下の設定をお勧めします。このコマンドは、作業ディレクトリ（`--work`）、出力ディレクトリ（`--out`）、一時ディレクトリ（`--temp`）を一度に設定し、ダウンロードしたクリップファイルを整理しやすくします。

```powershell
ChzzkClipDownloader clip_uid または url --work work --out out --temp temp
```

## JSON-RPCを使用した外部からの制御
詳細な情報については、`how_to_control_chzzk_clip_downloader.ja-JP.pdf`をご参照ください。

## お問い合わせ
Chzzk Downloader Suiteに関するご質問、バグ報告、または改善要望がございましたら、[GitHub]（https://github.com/Choonholic/ChzzkDownloader/）の[Issues]（https://github.com/Choonholic/ChzzkDownloader/issues/new）機能を通じてお知らせください。全ての言語に対応可能ですが、直接対応可能な言語は韓国語、英語、日本語、中国語です。他の言語については、機械翻訳を通じて対応するため、100%正確に対応できない場合があります。
