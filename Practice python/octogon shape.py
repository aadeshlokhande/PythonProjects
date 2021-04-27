# pip install turtle
from turtle import *
import time
# Author = TECH_IN_SECONDS

speed(0)
hideturtle()
bgcolor("black")
pensize(5)

color("yellow")
for i in range(8):
    left(45)
    for i in range(8):
        forward(100)
        right(45)
time.sleep(10)


# # creating a new dictionary
# my_dict = {"java": 100, "python": 112, "c": 11, "bhula":"cat"}

# # list out keys and values separately
# key_list = list(my_dict.keys())
# val_list = list(my_dict.values())

# # print key with val 100
# position = val_list.index("cat")
# print(key_list[position])

# # print key with val 112
# position = val_list.index(112)
# print(key_list[position])

# # one-liner
# print(list(my_dict.keys())[list(my_dict.values()).index(112)])


# print(my_dict.keys())

# dic = {"hello":"Hello ji", "gm":"Good morning", "ga":"Good Afternoon", "gn":"good night"}
#
# print(dic["gn"])