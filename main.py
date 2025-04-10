import telebot
import time
import threading

API_TOKEN = 'توکن_بات_تو_اینجا_بذار'
ADMIN_IDS = [7968070502, 5760993600]

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton("نیاز به مشاوره مهاجرتی دارم", callback_data="need_help")
    markup.add(btn)
    bot.send_message(message.chat.id, "سلام! به ربات مهاجرتی هرالد گروپ خوش آمدید.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "need_help":
        bot.send_message(call.message.chat.id, "لطفاً پیام خود را بنویسید.")
        bot.register_next_step_handler(call.message, forward_to_admins)

def forward_to_admins(message):
    for admin_id in ADMIN_IDS:
        bot.send_message(admin_id, f"پیام جدید:\nاز: @{message.from_user.username or 'ندارد'}\nآیدی: {message.from_user.id}\n\n{message.text}")

def send_advertisement():
    while True:
        try:
            CHANNELS = ["@channel_or_group_username"]
            for ch in CHANNELS:
                bot.send_message(ch, "این یک تبلیغ آزمایشی است که هر ۱۲ ساعت ارسال می‌شود.")
        except:
            pass
        time.sleep(43200)

threading.Thread(target=send_advertisement).start()
bot.infinity_polling()
