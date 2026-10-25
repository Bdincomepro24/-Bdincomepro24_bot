import os
import telebot
from telebot import types

# আপনার বটের টোকেন
BOT_TOKEN = "7963283287:AAHO4y9Ww2t8rW8WbL8O8W8bL8" # এখানে আপনার আসল বট টোকেন দিন
bot = telebot.TeleBot(BOT_TOKEN)

# গিটহাব পেজের মিনি অ্যাপ লিংক
WEB_APP_BASE_URL = "https://bdincomepro24.github.io/-Bdincomepro24_bot/index.html"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name or "ইউজার"
    
    # রেফারার আইডি চেক করা (/start 12345678)
    args = message.text.split()
    referrer_id = None
    if len(args) > 1:
        referrer_id = args[1].strip()

    # মিনি অ্যাপ URL তৈরি করা (রেফারার সহ)
    if referrer_id and str(referrer_id) != str(user_id):
        app_url = f"{WEB_APP_BASE_URL}?start={referrer_id}"
    else:
        app_url = WEB_APP_BASE_URL

    # ইনলাইন কিবোর্ড বাটন তৈরি
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo(url=app_url)
    btn_play = types.InlineKeyboardButton(text="🚀 অ্যাপ ওপেন করুন ও ইনকাম করুন", web_app=web_app)
    markup.add(btn_play)

    welcome_text = (
        f"স্বাগতম, {first_name}!\n\n"
        f"আমাদের মিনি অ্যাপে ভিডিও দেখে, গণিত সমাধান করে এবং স্পিন ঘুরিয়ে প্রতিদিন পকেট খরচ আয় করুন।\n\n"
        f"নিচের বাটনে ক্লিক করে কাজ শুরু করুন 👇"
    )

    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
