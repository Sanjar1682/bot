from flask import Flask
import threading
import telebot

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "salom bot ishlayapti", 200

# ======================================
# BOT
TOKEN = "5403407077:AAH4vjH8hhtBL3JKg8xgc1uzKO4n20lf4Gs"

bot = telebot.TeleBot(TOKEN)
# ======================================
# Botni kodlari

@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, "Salom, bot ishlavotd!")

# ======================================
#  Botni va Serverni ishga tushrsh

def run_bot():
    bot.polling(non_stop=True)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=5000, debug=True)
