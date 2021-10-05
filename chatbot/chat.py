from time import sleep

import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler
import requests

token = "1996409041:AAG9DCzYzX5QZL09gB_SkBPz3C6zi1D7Pxw"
id = "2010819287"

# updater
bot = telegram.Bot(token=token)
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

# 사용자가 보낸 메시지를 읽어들이고, 답장 전송
# 아래 함수만 입맛에 맞게 수정. 다른 것은 건들 필요 없음

def coin_message(): # 코인 시세 출력
    # request를 통해 api에 요청
    params = {'param1': 'value1', 'param2': 'value'}
    response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR', params=params)

    # 요청한 data를 slicing
    s = str(response.text)[7:15]

    usd = "BTC-USD : " + s
    return usd

def stop():
    updater.stop()

def handler(update, context):
    user_text = update.message.text # 사용자가 보낸 메시지를 user_text 변수에 저장
    if user_text == "안녕": # 사용자가 보낸 메시지가 "안녕"이라면?
        bot.send_message(chat_id=id, text="어 그래 안녕!") # 답장 보내기
    elif user_text == "뭐해?":
        bot.send_message(chat_id=id, text="공부중!") # 답장 보내기
    elif user_text == 'coin':
        bot.send_message(chat_id=id, text="코인 시세를 일려드립니다")
        while(1):
            bot.send_message(chat_id=id, text=coin_message())
            sleep(1)
            inter_text = update.message.text
            if(inter_text == '/stop'):
                bot.send_message(chat_id=id, text="출력을 중지합니다.")
                stop()
                break


bot.sendMessage(chat_id = id, text = "테스트 시작")
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)

