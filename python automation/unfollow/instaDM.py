from instabot import Bot
start = 0
end = 60
count = 1
list = []
a = open('DataFollowers.txt','r')
for aa in a:
    list.append(aa.replace("\n", ""))
while True:
    user60 = []
    for i in range(start,end):
        user60.append(list[i])


    bot = Bot()
    bot.login(username = "tech_in_seconds", password = "CyberInstagram<007>")

    bot.send_messages("Hello, are you a python lover if yes then follow : @tech_in_seconds",user60)

    start = start + 60
    end = end + 60
    print(count)
    count = count + 1