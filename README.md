
# Slack オウム返しBot

このプロジェクトは、Slackで動作するシンプルなオウム返しBotです。メンションされたメッセージをそのまま返信します。

## 前提条件

- Python 3.11
- pip (Pythonパッケージマネージャー)
- Node.js と npm (Serverless Frameworkのインストールに必要)
- AWS CLI (設定済みのAWSアカウント)
- Slackワークスペースの管理者権限

## セットアップ

1. リポジトリをクローンします：

   ```bash
   git clone https://github.com/yourusername/slack-echo-bot.git
   cd slack-echo-bot
   ```

2. 仮想環境を作成し、アクティベートします：

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
   ```

3. 依存関係をインストールします：

   ```bash
   pip install -r requirements.txt
   npm install -g serverless
   ```

## 手動デプロイ

1. Serverless Frameworkを使用してデプロイします：

   ```bash
   serverless deploy
   ```

2. デプロイ後、出力されるエンドポイントURLをコピーします。

3. Slack AppのEvent Subscriptionsを設定します：
   - Slack Appの設定ページで「Event Subscriptions」を有効にします。
   - Request URLにデプロイで得たエンドポイントURLを入力します。
   - 「Subscribe to bot events」で `app_mention` を追加します。
   - 変更を保存します。

これで、SlackワークスペースでBotにメンションすると、オウム返しで応答するようになります。

## 手動削除

プロジェクトを削除するには、以下の手順を実行します：

1. Serverless Frameworkを使用してスタックを削除します：

   ```bash
   serverless remove
   ```

2. Slack Appを削除します：
   - [Slack API](https://api.slack.com/apps)にアクセスします。
   - 該当するアプリを選択し、「Settings」→「Delete App」を実行します。

## トラブルシューティング

- デプロイに失敗する場合は、AWSの認証情報が正しく設定されているか確認してください。
- Botが応答しない場合は、Slack AppのOAuth & PermissionsページでBotトークンが正しく生成されているか確認してください。
- CloudWatchログを確認して、Lambda関数のエラーを調査することができます。

## 注意事項

- このプロジェクトはデモンストレーション目的で作成されています。本番環境で使用する前に、セキュリティとスケーラビリティを考慮した追加の設定を行ってください。
- AWS利用料金が発生する可能性があります。使用状況を定期的に確認してください。
