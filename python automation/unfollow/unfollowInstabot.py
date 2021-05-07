from instabot import Bot
from time import sleep
from random import randint

bot = Bot()

bot.login(username="tech_in_seconds", password="CyberInstagram<007>")

non_followers = set(bot.following) - set(bot.followers)

for non_follower in non_followers:
    try:
        bot.unfollow(non_follower)
        sleep(randint(6,12))
    except Exception as e:
        print(e)
        sleep(randint(30,150))