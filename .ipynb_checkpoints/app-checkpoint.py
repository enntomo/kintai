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
    
    global SP_SHEET
    SP_SHEET = atd_name

#     if atd_name == '遠藤':
#         SP_SHEET = '遠藤'
#     elif atd_name == '長﨑':
#         SP_SHEET = '長﨑'
#     elif atd_name == '荒井':
#         SP_SHEET = '荒井'
#     elif atd_name == '山田':
#             SP_SHEET = '山田'
#     elif atd_name == '山口':
#             SP_SHEET = '山口'
#     elif atd_name == '戸辺':
#             SP_SHEET = '戸辺'        
#     elif atd_name == '泉田':
#             SP_SHEET = '泉田'        
#     elif atd_name == '小泉':
#             SP_SHEET = '小泉'        
#     elif atd_name == '松岡':
#             SP_SHEET = '松岡'        
#     elif atd_name == '丁':
#             SP_SHEET = '丁'        
#     elif atd_name == '相澤':
#             SP_SHEET = '相澤'        
#     elif atd_name == '志村':
#             SP_SHEET = '志村'
#     elif atd_name == '宮川':
#             SP_SHEET = '宮川'        

        
        
        
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet





#出勤
def punch_in():
    worksheet =auth()
    df = pd.DataFrame(worksheet.get_all_records())
    
    name = atd_name
    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'名前': name, '日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
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

YOUR_CHANNEL_ACCESS_TOKEN = 'SoGDQ4I5JV4V2IPLMQjsdhCBTXnhir3EZtMy4sDkdMmAnSHuCtY4tYz6y36Rbni1iRQUR0jzrUJq65LxD8lc7gbatf8mk2es8GwhIsWasTmDClZl7nsWNw9mrWJEi659+3AB+tJDnH1RsUnXaa4U6QdB04t89/1O/w1cDnyilFU='
YOUR_CHANNEL_SECRET = '0aceaab59dbadc0b3a5fbd341082185d'

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
        
    elif '記録確認' in atd:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text= atd_name + df.iloc[:, 1:]))
    else: pass
        
if __name__ == "__main__":
    port = os.getenv("PORT")
    app.run(host="0.0.0.0", port=port)
    
    
    



