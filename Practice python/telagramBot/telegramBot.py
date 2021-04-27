from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

import constants as key
import Responses as Res

print("Start BOT...")

help_text = '''
| <😍> | <😍> | <😍> | <😍> | <😍> |\n
😎😎😎MAIN FEATURES😎😎😎\n
😎1) 💻 Wikipedia search \ntype: wiki <anytopic>\nExample:- wiki tajmahal\n
😎2) 🔤 Search a meaning of word \ntype: mean <anyword>\nExample:- mean World\n
😎3) 🔟 Convert number to words \ntype: word in <any number>\nExample:- word in 12\n
😎4) 🆔 Instagram ID details \ntype: insta <username>\nExample:- insta aadesh_lokhande\n
😎5) 💱 Translate to Hindi\ntype: trans <sentense>\nExample:- trans I love India\n
😎6) 🔗 URL shortener\ntype: url <url/link>\nExample:- url https://t.me/AGLokhande_bot \n
😎7) 🦠 Covid updated cases\ntype: covid <country name>\nExample:- \na) covid India\nb) covid world\n
😎8) Calculator\ntype: calc <Equation>\nExample:- calc 3+2-1*2\\6\n
😎9) Bitoin Price\ntype: Bitcoin\n
😎10) calender\nTypr: month <month number> <year>\nExample:- month 9 1997

😊😊😊BASIC FEATURES😊😊😊\n
😊1) ⌛️ Time \ntype: time\n
😊2) 🗓️ Date \ntype: date\n
😊3) 🆔 Instagram ID \ntype: instagram\n
😊4) 🅰️ Big word \ntype: big <any word>\nexample:- big Aadesh\n
😊5) 🙃 Reverse sentense\ntype: rev <any sentense>\nExample:- rev Aadesh Lokhande\n
😊6) 🔠 Capitalize sentense\ntype: cap <any sentense>\nExample:- cap Aadesh Lokhande\n
😊7) 🔡 Small letters\ntype: small <any sentense>\nExample:- small Aadesh Lokhande\n
😊8) 😉 Emoji\ntype: emoji <emoji>\nExample: emoji moon\n
😊9) 🗣️ You can do small talk also (Beta Version)\n
| <😍> | <😍> | <😍> | <😍> | <😍> |
'''


def start_command(update, context):
    update.message.reply_text("Welcome to Aadesh Lokhande's Bot.\nHow can I help you \n/help")

def help_command(update, context):
    update.message.reply_text(help_text)

def handle_command(update, context):
    text = str(update.message.text).lower()
    response = Res.sample_responses(text)
    helpmsg = Res.navigat(text)
    update.message.reply_text(response+"\n"+helpmsg)

def error(update, context):
    print(f"Update:- {update}\n\ncaused error:- {context.error}")

def main():
    updater = Updater(key.API_KEY, use_context= True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_command))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
    
main()
