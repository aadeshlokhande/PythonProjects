from instabot import Bot

bot = Bot()
bot.login(username = "asian_girls_villa", password = "Asian786")

file = open("uspython.txt",'r')
for username in file:
    try:
        bot.send_message(
            f'''Hello {username},
            check my profile and I hope you will like my profile 
            @asian_girls_villa ''',
            username
        )
    except:
        pass