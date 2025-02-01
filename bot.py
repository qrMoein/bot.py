import telebot

# اطلاعات ربات
TOKEN = "7831675413:AAGVSCfd2TP38e4JfyBnRld5xZZ-h6LyFic"
CHANNEL_ID = "@channel_username"  # https://t.me/jointestfirst

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def check_membership(message):
    user_id = message.from_user.id
    try:
        # بررسی وضعیت کاربر در کانال
        chat_member = bot.get_chat_member(CHANNEL_ID, user_id)
        if chat_member.status in ["member", "administrator", "creator"]:
            bot.send_message(message.chat.id, "✅ شما در کانال عضو هستید!")
        else:
            bot.send_message(
                message.chat.id, 
                f"🚨 لطفاً ابتدا در کانال عضو شوید: {CHANNEL_ID}"
            )
    except Exception as e:
        bot.send_message(message.chat.id, "❌ خطایی رخ داده است!")

bot.polling()
