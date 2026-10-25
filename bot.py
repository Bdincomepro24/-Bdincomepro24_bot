import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Config
BOT_TOKEN = "8841290203:AAHyF71CTbOf7Ptkx5wQgVOAk2rouMr6uz0"
BOT_USERNAME = "Bdincomepro24_bot"
# Replace with your new GitHub Pages or deployment URL
MINI_APP_URL = "https://privetrostom08-rgb.github.io/pocket-income/index.html"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    
    referrer_id = None
    if context.args and len(context.args) > 0:
        referrer_id = context.args[0]
        logger.info(f"User {user.id} joined via referrer: {referrer_id}")

    app_url = MINI_APP_URL
    if referrer_id:
        app_url = f"{MINI_APP_URL}?start={referrer_id}"

    welcome_text = (
        f"👋 **স্বাগতম, {user.first_name}!**\n\n"
        f"✨ **পকেট খরচ ইনকাম করুন** বটে আপনাকে স্বাগতম।\n"
        f"ইনভেস্ট ছাড়া খুব সহজে ছোট ছোট কাজ ও ভিডিও দেখে পকেট খরচ ইনকাম করুন।\n\n"
        f"💰 **পেমেন্ট সুবিধা:** মাত্র ৫০ টাকা বা $10 হলেই বিকাশ, নগদ বা USDT-তে সরাসরি পেমেন্ট নিতে পারবেন।\n\n"
        f"👇 কাজ শুরু করতে নিচের **'🚀 ওপেন অ্যাপ'** বাটনে চাপ দিন:"
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 ওপেন অ্যাপ (কাজ শুরু করুন)", 
                web_app=WebAppInfo(url=app_url)
            )
        ],
        [
            InlineKeyboardButton(
                "👥 বন্ধুদের ইনভাইট করুন", 
                url=f"https://t.me/share/url?url=https://t.me/{BOT_USERNAME}?start={user.id}&text={user.first_name}%20আপনাকে%20ইনভাইট%20করেছে!%20ছোট%20কাজ%20করে%20পকেট%20খরচ%20ইনকাম%20করুন।"
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text=welcome_text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    logger.info("Bot is running...")
    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
