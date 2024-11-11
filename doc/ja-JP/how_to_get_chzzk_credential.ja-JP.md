# Chzzk認証資格情報の取得方法

1. Microsoft Edge、Google Chrome、Mozilla Firefoxなどのデスクトップウェブブラウザで[Chzzk](https://chzzk.naver.com/)にアクセスします。
2. NAVER IDでログインします。
3. **Ctrl+Shift+I**を押して開発者ツールを開きます。
4. **アプリケーション**タブに移動します。
5. カテゴリの**クッキー**項目から**https://chzzk.naver.com**を選択します。
6. **NID_AUT**と**NID_SES**の値をコピーします。
7. 要求された際に、対応するフィールドに値を貼り付けます。

<div style='text-align: center'>
<img src='../../img/screenshots/dev_tools.png' />
<p><i>(この画像は最新の情報と異なる場合があります。)</i></p>
</div>

**[お知らせ]**
`NID_SES`の値はChzzkにログインするたびに変更されます。しかし、`NID_AUT`の値が有効である限り、毎回`NID_SES`の値をリセットする必要はありません。
