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
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    SP_SHEET_KEY = '1-YncoBYoSOqfSXP_W7bAuDJ-9MdtiWk6rTCgr5oIeBc'
    
    if atd_name == '遠藤'
        SP_SHEET = '遠藤'
    elif atd_name == '長崎'
        SP_SHEET = '長崎'
        
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet


app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = 'xaD08TJKexbs26kL74LkJWmkCYPbhI+FusQz9Nt2sl4tFxxSeHRNUf2Y2/Y8dUpC896jf216rsAgA0y5A8oiITm8Ze7LLtGZ8/IRhHHYL/k3+jepuf28lDMlwFEmkrb/v3at7UFRgHeiZZ2Rw69iSQdB04t89/1O/w1cDnyilFU='
YOUR_CHANNEL_SECRET = '734eb0b218d1ad81df88d46495d05ba0'

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
            TextSendMessage(text= atd_name + '出勤完了しました！'))
       
    elif '退勤' in atd:
        punch_out()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text= atd_name + '退勤しました！'))
    else: pass
        
if __name__ == "__main__":
    port = os.getenv("PORT")
    app.run(host="0.0.0.0", port=port)
    
    
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
    
#     df_name = df[df['名前'].str.contains(atd_name)].copy()
#     df_name.iloc[-1, 3] = punch_out
    
#     df_name = df[(df['遠藤'] == atd_name) & (df['退勤時間'] == '00:00')].replace({'退勤時間': {'00:00': punch_out}})
#     df_name = df[(df['名前'] == atd_name) & (df['退勤時間'] == '00:00')].replace({'退勤時間': {'00:00': punch_out}})
    
    
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')
    
    
    









        





