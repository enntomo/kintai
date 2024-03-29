from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import os

import pandas as pd
from datetime import datetime
import gspread

from oauth2client.service_account import ServiceAccountCredentials


def auth():
    SP_CREDENTIAL_FILE = ''
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = 'YOUR_SP_SHEET_KEY'
    
    global SP_SHEET
    SP_SHEET = atd_name

        
        
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet





#出勤
def punch_in():
    worksheet =auth()
    df = pd.DataFrame(worksheet.get_all_records())
    
    
    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'名前': atd_name, '日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out():
    worksheet =auth()
    df = pd.DataFrame(worksheet.get_all_records())
    
    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')
    df.iloc[-1, 3] = punch_out
        
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')


        

app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = 'YOUR_CHANNEL_ACCESS_TOKEN'
YOUR_CHANNEL_SECRET = 'YOUR_CHANNEL_SECRET'

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/")
def hello_world():
    return "hello world"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    attendance =  event.message.text
    atd = attendance.split()
    
    global atd_name
    atd_name = atd[0]
    
    if '出勤' in atd:
        punch_in()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text= atd_name + 'さん出勤完了です！今日も一日頑張りましょう！'))
       
    elif '退勤' in atd:
        punch_out()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text= '退勤完了！' + atd_name + 'さんお疲れ様でした！'))
    else: pass
        
if __name__ == "__main__":
    port = os.getenv("PORT")
    app.run(host="0.0.0.0", port=port)
    
    
    



