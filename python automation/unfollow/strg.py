list = []
a = open('DataFollowers.txt','r')
for aa in a:
    list.append(aa.replace("\n", ""))

user60 = []
for i in range(60):
    user60.append(list[i])

print(user60)