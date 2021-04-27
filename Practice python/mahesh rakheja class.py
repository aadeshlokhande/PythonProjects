#print('hello world')


# a = int(input('enter value for a : '))
# b = int(input('enter value for b : '))
# c = a + b
# print(c)
# print(type(a))
# print(type(b))



# how to print str and int
# dollers = input('enter the value in dollers = ')
# rupees = int(dollers) * 75
# print('amount in rupees is = '+ str(rupees))




# if condition
# age = int(input("Enter your age = "))
# if age>=18:
#     print("Munni Badnam Hue Darling Tere Liye")
# else:
#     print("Nanne Mune Bache Tere Muthi Me Kya Hai")





# age = int(input("Enter your age = "))
# gender = input('type your gender = ')
# if (age>=18 and gender == 'female') or (age>=21 and gender == 'male'):
#     print("YES...!! You Are Not Eligible")
# else:
#     print("NO...!! You Are Not Eligible")




# nasted if
# age = int(input("Enter your age = "))
# gender = input('type your gender = ')
# if gender == 'male':
#     if age>=21:
#         print('Eligible')
#     else:
#         print('not Eligible')
# elif gender == 'female':
#     if age == 18:
#         print("Eligible")
#     else:
#         print('Not Eligible')
# else:
#     print('Invalid Input')




# for loop (finite loop)
# for i in range(2,51,3):
#     print(i)

# for i in range(50,0,-2):
#     print(i)





# for i in range(1,200):
#     if i==20:
#         continue
#     if i == 40:
#         break
#     print(i)




# while loop (infanite loop)
# n=10
# while n<20:
#     print('hello')
#     n=n+1



# list(arrey)
# mylist = ['aadesh' , 'nilesh', 'suresh',10,23,34]
# print(mylist)

# print(list(range(0,15,3)))

# for i in [23,12,123,43,2,124,124,123,241,23,123]:
#     print(i, end = "\t")          # ("\t" for tab) and ("\n" for new line)




# Strings
# name = input("Enter Your Name = ")
# print(name)
# # print(name[0])
# # print(name[1])
# for i in name[::-1]:
#     print(i)
# print(len(name))            # lenth of str
#



# str sliceing
# sentence = "i hate you but i love you, i hate you but i love you , i hate you but i love you"
# print(sentence[0:10])
# print(sentence[:10])
# print(sentence[10:])
# print(sentence[:])
# print('i' not in sentence)


# sentence = "I hate you but I love you"
# print('sentence = ' + sentence)
#
# upsen = sentence.upper()
# print('upper = ' + upsen)
#
# tisen = sentence.title()
# print('title = ' + tisen)
#
# casen = sentence.casefold()
# print('casefold = ' + casen)
#
# cosen = sentence.capitalize()
# print('capitalize = ' + cosen)
#
# resen = sentence.replace('hate', 'love')
# print('replace = ' + resen)
#
# word = sentence.split()
# print(word)
#
# word1 = sentence.split('but')
# print(word1)




# # FUNCTION
#
# # Fruitful function
# def addition(a,b):
#     c = a + b
#     print(c)
#
# # non-fruitful function
# def substraction(a,b):
#     c = a - b
#     return c
#
# # addition(12,35)
# # output = substraction(32,12)
# # print(output)
#
# def operation(a,b):
#     add = a+b
#     sub = a-b
#     return add,sub
#
# # output = operation(10,5)
# # print(output)               #direct output
#
# a,s = operation(10,5)
# print(a)
# print(s)                       #one by one output




# # FILE OPERATION
#
# # 1) write
# # fhandle = open('readme.txt','w')
# # fhandle.write('what is your name?')
# # fhandle.close()
#
# # 2) apend
# # fhandle = open('readme.txt','a')
# # fhandle.write('\nMy Name Is Aadesh Lokhande.')
# # fhandle.close()
#
# # 3) read
# # fhandle = open('readme.txt')
# # data = fhandle.read()
# # print(data)
# # fhandle.close()                     # all at once
#
# # fhandle = open('readme.txt')
# # for line in fhandle:
# #     print(line)
# # fhandle.close()                     # line by line
#
# # fhandle = open('readme.txt')
# # data = fhandle.read()
# # if 'aadesh' in data:
# #     print('Yes, Present')
# # else:
# #     print('Not, Present')            # searching word
#
#
# # fhandle = open('readme.txt')
# # data = fhandle.read()
# # value = input("Enter a word to search = ")
# # if value in data:
# #     print('Yes, Present')
# # else:
# #     print('Not, Present')            # searching word by user
#
# # fhandle = open('readme.txt')
# # counter = 0
# # for li
# # ne in fhandle:
# #     counter = counter + 1
# # print(counter)                          #count lines in file
#
# # with open('readme.txt') as fhandle:
# #     for line in fhandle:
# #         print(line)                       #read file using "with" function


# # Data Structures
#
# #Program - Algorithm or Data structure
# # 1) list
# # 2) Dictionary
# # 3Tuple
# # 4)Set
#
# # schoolfds = ['rahul','aadesh', 'shubham','nilesh']
# # print(schoolfds[0])
# # print(schoolfds[1])
# # for i in schoolfds:
# #     print(i)
# # schoolfds[0] = 'sudhir'
# # print(schoolfds)
#
# # schoolfds = ['rahul','aadesh', 'shubham','nilesh']
# # clgfds = ['pranjal', 'sapna','diksha','vijya']
# # allfds = schoolfds + clgfds
# # name = input('enter  your name = ')
#
# # print(name in allfds)
# # if name in allfds:
# #     print('yes')
# # else:
# #     print('no')
#
# # print(allfds)
# # print(allfds[1:4])
# # print(allfds[1:])
# # print(allfds[:4])
# # print(allfds[:])
#
# # schoolfds = ['rahul','aadesh', 'shubham','nilesh']
# # clgfds = ['pranjal', 'sapna','diksha','vijya']
# # allfds = schoolfds+ clgfds
# #
# # for i in range(0,2):
# #     print(allfds[i])
#
# # print(len(allfds))
# # clgfds.append('zeenat')             #add a value
# # clgfds.remove('vijya')              #remove the value
# # clgfds.insert(2,'priya')            #insert a value
# # clgfds.pop(3)                       #remove by index
# # print(clgfds)



# # Dictionary
# price = {'soap':10, 'surf':15,'milk':20, 'brush':25}
# print(price)
#
# # print(price['milk'])
# # print(price['surf'])
# # for i in price:
# #     print(i,price[i])
#
# # if 'milk'in price:
# #     print('yes')
# # else:
# #     print('no')
#
# # price['eggs'] = 5
# # print(price)
# # del price['milk']
# # print(price)
#
# fhandle = open('readme.txt')        #open the file
# data = fhandle.read()               #read the file
# words = data.split()                #dpliting the data
# mydict = dict()
# for word in words:
#     if word not in mydict:
#         mydict[word] = 1
#     else:
#         mydict[word] = mydict[word] + 1
# print(mydict)
# fhandle.close()
#
# # price = {'soap':10, 'surf':15,'milk':20, 'brush':25}
#
# # value = price.get('milk','nope')
# # print(value)
#
# # keys = price.keys()
# # print(keys)
# # values = price.values()
# # print(values)



# # Tuple
#
# a,b,c = (1,2,3,)
# print(a)
# print(b)
# t1 = (2,3,2,23,4,1,4,3)
# t2 = (1,23,23,13,34,12)
# print(t1>t2)
# price = {'soap':10, 'surf':15,'milk':20, 'brush':25}
# items = price.items()
# print(items)











