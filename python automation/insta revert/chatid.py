def username():
    file = open('chat.txt','r')
    chat = file.readlines()

    usernames = []
    for line in chat:
        line01 = line.replace(" ", "*")
        line02 = line01.replace("\n","*")
        line = line02.split("*")
        
        for word in line:
            try: 
                if word[0] == "@":
                    usernames.append(word)
            except:
                pass
    return list(set(usernames))