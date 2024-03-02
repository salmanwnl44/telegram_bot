from telebot import TeleBot

# Replace with your bot's access token
bot = TeleBot("7040271479:AAEkbnMyheErbaV3qrOD_SoKt1tFWZ0psrg")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hi! I welcome newcomers to the group, Please join our channel https://t.me/+BLrELZvmD0Y1YzE1")

@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def greet_newcomer(message):
    new_members = message.new_chat_members
    for new_member in new_members:
        first_name = new_member.first_name
        last_name = new_member.last_name

        # Check if last name exists
        if last_name:
            welcome_message = f"Welcome, {first_name} {last_name}, Please join our channel https://t.me/+BLrELZvmD0Y1YzE1"
        else:
            welcome_message = f"Welcome, {first_name}, Please join our channel https://t.me/+BLrELZvmD0Y1YzE1"

        bot.send_message(message.chat.id, welcome_message)

# Start polling for incoming messages
try:
    bot.infinity_polling()
except Exception as e:
    print(f"An error occurred: {e}")
