from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os


app = Flask(__name__)


line_bot_api = LineBotApi()
handler = WebhookHandler()


@app.route("/")
def hello():
    return "Hello, World!"



@app.route("/api/dirupdate", methods=["POST"])
def recive():
    name = request.data
    print(name.decode('utf-8'))
    return name


@app.route("/api/test" , methods=['POST'])
def testapi():
  try:
    msg = request.data   # 取得網址的 msg 參數
    if msg != None:
      msg_data = msg.decode("utf-8")
      # 如果有 msg 參數，觸發 LINE Message API 的 push_message 方法
      line_bot_api.push_message(, TextSendMessage(text=msg_data))
      print(msg)
      return msg
    else:
      return 'OK'
  except:
    print('error')

if __name__ == "__main__":
    port = 5000
    app.run(host='0.0.0.0', port=port)