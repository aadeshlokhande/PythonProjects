
# # Static

# print("1 to 10 table")

# for i in range(1,11):
#     print("\t")
#     for j in range(1,11):
#         print(i*j, end= "\t" )
#     print("\t")



#
# User
# print("\n-------------tables between 2 numbers-----------------\n")
#
# mini = int(input("Enter 1st value =  "))
# maxi = int(input("Enter 2nd value =  "))
# 
# if mini < maxi:

#     for i in range(1, 11):
#         print("\t")
#         for j in range(mini, maxi + 1):
#             print(i * j, end="\t")
#         print("\t")

# else:
#     for i in range(1, 11):
#         print("\t")
#         for j in range(maxi, mini + 1):
#             print(i * j, end="\t")
# #         print("\t")
# print("Wrong Input")





# x = "123463"
# d = x[1] + x[4]
# print(d)





# # Emoji
# import emojis
#
# print(emojis.encode(":boat:"))
# print(emojis.encode(":sunny:"))
# print(emojis.encode(":heart:"))
# print(emojis.encode(":star:"))



# x = "py❤"
# y = x * 2
# z = "I love "
# print(z+y)



# number = 10
#
# number *= 2
# number /= 2
# print(number)
#
# number = 10
#
# number <<= 1
# number >>= 1
# print(number)



# ---------------if else ladder---------------
# age = int(input("Enter your age = "))
# if age < 100 and age > 7:
#     if age < 18:
#         print("You are not eligible for driving")
#     elif age > 18:
#         print("You are eligible for driving")
#     else:
#         print("meet physically")
# else:
#     print("invalid input")
#



# dict ={"java":100, "python":112, "c":11}
#
# key = list(dict.keys())
# val = list(dict.values())
#
# print(key[val.index(112)])


# surname
# key = list(dict.keys())
# val = list(dict.values())
# print(key[val.index("Lokhande")])

# name
# name = input("Enter your name = ")
# print(dict[name])



# --------------Dict exercise--------------

# dict = {"Aadesh":"Lokhande", "Nilesh":"Rangari", "Rohit":"Bansod", "Akash":"Wandre"}
# fol = input("You want to enter first name or last name = ")
# if fol == "last name":
#     lastname = input(" Enter : ")
#     key = list(dict.keys())
#     val = list(dict.values())
#     print(key[val.index(lastname)],lastname)
# elif fol =="first name":
#     firstname = input("Enter : ")
#     print(firstname,dict[firstname])
# else:
#     print("invalid input")





# #---------chrome dino game---------
# import pyautogui
# from PIL import Image, ImageGrab
# import time
#
# def screenshot():
#     img = ImageGrab.grab().convert('L')
#     return img
#
# def press(key):
#     pyautogui.keyDown(key)
#     return
#
# def detect(data):
#     for i in range(485,525):
#         for j in range(220,260):
#             press('up')
#             return
#
# press('up')
# time.sleep(2)
# while True:
#     img = screenshot()
#     data = img.load()
#     detect(data)





# # ----------------practice question-----------------
# list = ["asd", 45, 8,"af", 44,1,55,22,4,22,"shubham", "aadesh",15,5]
#
# for a in list:
#     if str(a).isnumeric() and a > 6:
#         print(a)






# ---------------------print numbers without using Range Funtion---------------
# a = 1
# while True:
#     if a <12:
#         print(a)
#     else:
#         break
#     a = a+1



# ------------Tables between min to max numbers-----------
# a= int(input("Enter = "))
# b = int(input("Enter = "))
# for i in range(1, 11):
#     print("\t")
#     for j in range(a, b + 1):
#         print(i * j, end="\t|\t")




# ------------Tables between two numbers-------
# a= int(input("Enter = "))
# b = int(input("Enter = "))
# if a<b:
#     for i in range(1, 11):
#         print("\t")
#         for j in range(a, b + 1):
#             print(i * j, end="\t|\t")
# else:
#     for i in range(1, 11):
#         print("\t")
#         for j in range(b, a + 1):
#             print(i * j, end="\t|\t")





# ------------print pattern-----------
# ~~~~~~~~~OUTPUT~~~~~~~~~
# 1
# 22
# 333
# 4444
# 55555
# 6666666

# ~~~~~~~~PROGRAM~~~~~~~~~

# n = int(input("Enter = "))
# x = 0
# for i in range(1 , n+1):
#     x += 1
# for j in range(1, i + 1):
#     print(x , end=" ")








a = "Aadesh"
print(type(a))
