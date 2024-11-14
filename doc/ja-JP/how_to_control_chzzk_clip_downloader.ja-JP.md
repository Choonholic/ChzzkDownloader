# Chzzk Clip Downloaderを外部からJSON-RPCで制御する方法

## Chzzk Downloader Suite JSON-RPC 仕様
Chzzk Downloader Suiteは、外部からの制御を可能にするために、[JSON-RPC 2.0 仕様](https://www.jsonrpc.org/specification)に準拠した単一リクエストをサポートしています。

## サーバーへの接続方法
内部JSON-RPCサーバーはソケット接続を受け付けます。

* **ホストIPアドレス** - デフォルトのアドレスは`localhost`です。
* **ポート番号** - デフォルトのポート番号は`64000`です。`--rpcport`オプションで変更可能です。（有効範囲: `49152`〜`65300`）
* **RPC ID** - デフォルトのIDは`50`です。`--rpcid`オプションで変更可能です。

## リクエストの方法
Chzzk Clip Downloaderにアクションをリクエストするには、次のようなオブジェクトをソケット経由で送信します。

```json
{
    "jsonrpc": "2.0",
    "method": "get_status",
    "id": 50
}
```

### メソッド一覧
* `get_info` - 全情報を一括で取得します。
* `get_version` – アプリケーションのバージョンを取得します。
* `get_settings` – アプリケーションの設定を取得します。
* `get_channel` – チャンネル情報を取得します。
* `get_clip` – クリップが現在ダウンロード中の場合、クリップ情報を取得します。
* `get_status` – 現在のステータスを取得します。
* `set_settings` – アプリケーションの設定を変更します。
* `reload_settings` – 設定ファイルからアプリケーションの設定を再読み込みします。
* `quit_app` – 現在のダウンロード（進行中の場合）を停止し、アプリケーションを終了します。

## レスポンス
Chzzk Clip Downloaderは、以下の形式でレスポンスを返します。

```json
{
    "jsonrpc": "2.0",
    "result": "Success",
    "id": 50
}
```

### リクエストが正常に処理された場合
* `result` - リクエストされたメソッドの結果を示します。

### リクエストが正しく処理されなかった場合
* `error` - レスポンスがエラーであることを示します。
* `code` - エラー コード。
* `message` - エラー メッセージ。

## サンプル
GitHubリポジトリ内の[samples](https://github.com/Choonholic/ChzzkDownloader/blob/main/samples/)を参照してください。
