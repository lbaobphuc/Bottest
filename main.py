from flask import Flask, request
import telegram
import os

TOKEN = os.environ.get("8055106598:AAEWKlquZsNGrA2mKiPZ7yjqSO_9smuSNsU")
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot hoạt động rồi nè!")

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    msg = update.message.text
    bot.send_message(chat_id=chat_id, text=f"Bạn nói: {msg}")
    return "ok"

if __name__ == "__main__":
    app.run()
