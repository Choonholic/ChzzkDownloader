# Slack通知プラグイン

このプラグインは、Slackユーザーにメッセージを送信します。

## 初期設定

### Webhook URLを作成する

1. [Slack API: Incoming Webhooks](https://api.slack.com/messaging/webhooks)にアクセスし、「**Create your Slack app**」をクリックします。
2. アプリ名と、メッセージを投稿する対象のSlackワークスペースを選択して、アプリを作成します。
3. 作成したアプリのダッシュボードで、左側の「**Incoming Webhooks**」を選択します。
4. 「**Activate Incoming Webhooks**」を**オン**に切り替えます。
5. ページ下部の「**Add New Webhook to Workspace**」をクリックし、メッセージを投稿したいチャンネルを選択して許可します。
6. Webhook URLが表示されるので、コピーして安全な場所に保存してください。

### プラグインを初期化する

1. `pn_slack.exe`ファイルがあるディレクトリに`pn_slack.json`というファイルが存在する場合は、`pn_slack.json.bak`に名前を変更するか削除してください。
2. `pn_slack.exe`ファイルを実行します。
3. `Please enter your Slack webhook URL:`と表示されたら、先ほどコピーしたWebhook URLを貼り付けて入力します。

## テストする
コマンドプロンプトまたはPowerShellで、以下のように実行してメッセージが正しく送信されるか確認します。

```powershell
.\pn_slack.exe "メッセージ送信テスト"
```

## 制約事項
このプラグインは、`plain`または`slack`の通知テキスト形式のみをサポートします。
