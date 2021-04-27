from telegram import *
from telegram.ext import *

bot = Bot("1419399324:AAFLj0oSPXuYNk6AcQp14BHu1q6nxcmcrKA")

updater = Updater("1419399324:AAFLj0oSPXuYNk6AcQp14BHu1q6nxcmcrKA", use_context=True)
dispacher = updater.dispatcher
print(bot.get_me())


# reply commands
# start
def start( update : Update ,context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="/Hello - Say hello\n/Instagram - instagram id"
    )
print(bot.get_me())
start_value = CommandHandler("start",start)
dispacher.add_handler(start_value)

# Hello
def hello( update : Update ,context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello its me Aadesh Lokhande... \nthis message send automatically....",
    )
print(bot.get_me())
start_value = CommandHandler("Hello",hello)
dispacher.add_handler(start_value)


# insagram
def insta_id( update : Update ,context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="instagram.com/aadesh_lokhande",
    )
print(bot.get_me())
start_value = CommandHandler("Instagram",insta_id)
dispacher.add_handler(start_value)













updater.start_polling(poll_interval=0.1)