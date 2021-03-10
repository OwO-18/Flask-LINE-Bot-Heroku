import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text='Hello World!')
    
    if event.message.text == "喵":
        url = 'https://blog.accupass.com/wp-content/uploads/2017/03/1_120122230539_1.jpg'
        image_message = ImageSendMessage(
            original_content_url = url,
            preview_image_url = url
        )
        line_bot_api.reply_message(event.reply_token, image_message)
        return 0
    
    elif event.message.text == "喵喵":
        reply = TextSendMessage(text = '汪汪')
        line_bot_api.reply_message(event.reply_token, reply)
        
    elif event.message.text == "第一關":
        url = 'https://i.imgur.com/iSNZt1l.png'
        image_message = ImageSendMessage(
            original_content_url = url,
            preview_image_url = url
        )
        line_bot_api.reply_message(event.reply_token, image_message)
        return 0

    if event.message.text == "start":
        task_fail = true
        while task_fail:
            if stage_1() == 1
                reply = TextSendMessage(text = '恭喜答對')
                line_bot_api.reply_message(event.reply_token, reply)
                task_fail = false
            
            if stage_1() == 0
                reply = TextSendMessage(text = '不對噢')
                line_bot_api.reply_message(event.reply_token, reply)
        
        reply = TextSendMessage(text = '第二關')
        line_bot_api.reply_message(event.reply_token, reply)
    
    line_bot_api.reply_message(event.reply_token, reply)

def stage_1():
    story = TextSendMessage(test = '第一段故事')
    line_bot_api.reply_message(event.reply_token, story)
    
    if event.message.text == "答案“:
        reply = TextSendMessage(text = '恭喜答對')
        line_bot_api.reply_message(event.reply_token, reply)
        return 1
        
    else 
        reply = TextSendMessage(text = '不對喔')
        line_bot_api.reply_message(event.reply_token, reply)
        return 0
                                
    
    
    
    
