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


#遠藤
def auth_endo():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '1t3PNpGmPeBUOEXhYoC7Env8HacU_fdx-km32s5cRhI4'
    SP_SHEET = '遠藤'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

    #出勤
def punch_in_endo():
    worksheet =auth_endo()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
    #退勤
def punch_out_endo():
    worksheet =auth_endo()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')

#長崎
def auth_naga():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '1-YncoBYoSOqfSXP_W7bAuDJ-9MdtiWk6rTCgr5oIeBc'
    SP_SHEET = '長崎'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in_naga():
    worksheet =auth_naga()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out_naga():
    worksheet =auth_naga()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')

#戸部
def auth_tobe():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '1d2tnZZlt0nN4Y86A3HqaECyk-c5qr1f-C99jy7UnanU'
    SP_SHEET = '戸部'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in_tobe():
    worksheet =auth_tobe()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out_tobe():
    worksheet =auth_tobe()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')

#荒井
def auth_arai():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '1nXaKIRO0fPYcNVZXxFY9lBfy6ciXUYqyDdswTX153bQ'
    SP_SHEET = '荒井'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in_arai():
    worksheet =auth_arai()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out_arai():
    worksheet =auth_arai()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')

#山田
def auth_yamada():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '1O-TeCpE3FJEV-Gmv98tuTpaQaandRNf-pMCGdeHz07c'
    SP_SHEET = '山田'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in_yamada():
    worksheet =auth_yamada()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out_yamada():
    worksheet =auth_yamada()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')

#山口
def auth_yama():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '1C5VYDXm6pPuHUbXy3R_gGxETHQ052Y5vRNvCk-ycFNY'
    SP_SHEET = '山口'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in_yama():
    worksheet =auth_yama()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out_yama():
    worksheet =auth_yama()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')

#宮川
def auth_miya():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '1jVzFy_PXkRY0e4SimVT9XmScpTuCSn7LgHf0-U-R1_Q'
    SP_SHEET = '宮川'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in_miya():
    worksheet =auth_miya()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out_miya():
    worksheet =auth_miya()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')

#志村
def auth_simu():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '1WQaprbXPwtgOLJmyYz2W458XvEjsiXFGi5834zWuFIs'
    SP_SHEET = '志村'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in_simu():
    worksheet =auth_simu()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out_simu():
    worksheet =auth_simu()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')

#丁
def auth_tei():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '12nRcIZdSgZE5PgjVRJ3Q1UQI2a-MNZJ9NLlN48oAVGE'
    SP_SHEET = '丁'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in_tei():
    worksheet =auth_tei()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out_tei():
    worksheet =auth_tei()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')

#泉田
def auth_izu():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '1rMLs8CJEwmHDhiXa7pu3HahivIkhbzq-wioqtQ8Zs4E'
    SP_SHEET = '泉田'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in_izu():
    worksheet =auth_izu()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out_izu():
    worksheet =auth_izu()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')

#小泉
def auth_koi():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '1HKfXF49yLmHASSeHJbR4hNRO-qn5fDn2sOdTgjAuR6A'
    SP_SHEET = '小泉'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in_koi():
    worksheet =auth_koi()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out_koi():
    worksheet =auth_koi()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')

#松岡
def auth_matu():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '18aWh07IJVzUeGtChYkYkRxjkk-6BzvfBe4kjute-qVk'
    SP_SHEET = '松岡'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in_matu():
    worksheet =auth_matu()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out_matu():
    worksheet =auth_matu()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')

#相澤
def auth_ai():
    SP_CREDENTIAL_FILE = 'job.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = '1-92xIqnVpKhTnnKJ_nSNVI8zIPCvQYZ3aQtRpwxsSNk'
    SP_SHEET = '相澤'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in_ai():
    worksheet =auth_ai()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間': punch_in, '退勤時間': '00:00'}, ignore_index=True)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print('出勤完了しました！')
#退勤
def punch_out_ai():
    worksheet =auth_ai()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('退勤しました！')



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
    if '遠藤' in event.message.text:
        if '出勤' in event.message.text:
            punch_in_endo()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
        elif '退勤' in event.message.text:
            punch_out_endo()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='退勤しました！'))
    elif '長崎' in event.message.text:
        if '出勤' in event.message.text:
            punch_in_naga()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
        elif '退勤' inevent.message.text:
            punch_out_naga()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='退勤しました！'))

    elif '戸部' in event.message.text:
        if '出勤' in event.message.text:
            punch_in_tobe()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
        elif '退勤' inevent.message.text:
            punch_out_tobe()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='退勤しました！'))

    elif '荒井' in event.message.text:
        if '出勤' in event.message.text:
            punch_in_arai()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
        elif '退勤' inevent.message.text:
            punch_out_arai()
            line_bot_api.reply_message(
                event.reply_token,

    elif '山田' in event.message.text:
         if '出勤' in event.message.text:
            punch_in_yamada()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
         elif '退勤' inevent.message.text:
            punch_out_yamada()
            line_bot_api.reply_message(
                event.reply_token,

    elif '山口' in event.message.text:
         if '出勤' in event.message.text:
            punch_in_yama()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
         elif '退勤' inevent.message.text:
            punch_out_yama()
            line_bot_api.reply_message(
                event.reply_token,

    elif '宮川' in event.message.text:
         if '出勤' in event.message.text:
            punch_in_miya()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
         elif '退勤' inevent.message.text:
            punch_out_miya()
            line_bot_api.reply_message(
                event.reply_token,          


    elif '志村' in event.message.text:
         if '出勤' in event.message.text:
            punch_in_()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
         elif '退勤' inevent.message.text:
            punch_out_()
            line_bot_api.reply_message(
                event.reply_token,           


    elif '丁' in event.message.text:
         if '出勤' in event.message.text:
            punch_in_tei()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
         elif '退勤' inevent.message.text:
            punch_out_tei()
            line_bot_api.reply_message(
                event.reply_token,            


    elif '泉田' in event.message.text:
         if '出勤' in event.message.text:
            punch_in_izu()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
         elif '退勤' inevent.message.text:
            punch_out_izu()
            line_bot_api.reply_message(
                event.reply_token,            


    elif '小泉' in event.message.text:
         if '出勤' in event.message.text:
            punch_in_koi()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
         elif '退勤' inevent.message.text:
            punch_out_koi()
            line_bot_api.reply_message(
                event.reply_token,

    elif '松岡' in event.message.text:
         if '出勤' in event.message.text:
            punch_in_matu()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
         elif '退勤' inevent.message.text:
            punch_out_matu()
            line_bot_api.reply_message(
                event.reply_token,             

    elif '相澤' in event.message.text:
         if '出勤' in event.message.text:
            punch_in_ai()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤完了しました！'))
         elif '退勤' inevent.message.text:
            punch_out_ai()
            line_bot_api.reply_message(
                event.reply_token,            
                
    else: pass           
                
                
if __name__ == "__main__":
    port = os.getenv("PORT")
    app.run(host="0.0.0.0", port=port)
                
                
                
                