import os
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler

# Slack Boltアプリケーションの初期化
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.event("app_mention")
def handle_mention(event, say):
    """
    Botへのメンション時の処理を行う関数

    Args:
        event (dict): Slackイベントの詳細情報
        say (callable): メッセージを送信するための関数

    Returns:
        None

    Raises:
        Exception: メッセージの送信に失敗した場合
    """
    try:
        # メンションされたテキストを抽出
        text = event['text']
        mention_text = text.split('>')[1].strip()

        # オウム返しメッセージを送信
        say(f"あなたが言ったのは: {mention_text}")
    except IndexError:
        # メンションテキストの抽出に失敗した場合
        say("申し訳ありません。メッセージを正しく解析できませんでした。")
    except Exception as e:
        # その他の予期せぬエラーが発生した場合
        print(f"エラーが発生しました: {str(e)}")
        say("申し訳ありません。エラーが発生しました。")

def handler(event, context):
    """
    AWS Lambdaのハンドラー関数

    Args:
        event (dict): AWS Lambdaイベント
        context (object): AWS Lambdaコンテキスト

    Returns:
        dict: Slack APIレスポンス

    Raises:
        Exception: Slackイベントの処理に失敗した場合
    """
    try:
        # SlackRequestHandlerを使用してイベントを処理
        slack_handler = SlackRequestHandler(app=app)
        return slack_handler.handle(event, context)
    except Exception as e:
        # 予期せぬエラーが発生した場合
        print(f"Lambdaハンドラーでエラーが発生しました: {str(e)}")
        return {
            "statusCode": 500,
            "body": "Internal Server Error"
        }
