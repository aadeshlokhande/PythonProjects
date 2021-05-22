file = open('id.txt',"r")
usernames = file.readlines()
print(len(usernames))
# for i in usernames:
#     print(i,end="")
print("\n\n\n")
print(len(set(usernames)))