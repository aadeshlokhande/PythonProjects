
# Problem number 7
# a = input("file name = ")
# b = a.split(".")
# print(b[1])

# problem number 8
# a = ["red", "white", "yellow", "black"]
# print(a[0],a[-1])


# # Problem numberconvert seconds in minutes
# a= int(input("Enter seconds = "))
# h = a/3600
# hm = a%3600
# m = hm/60
# s = hm%60
#
# if a >= 3600:
#     print(str(int(h)) +" Hours "+ str(int(m)) +" Minutes & "+ str(int(s))+" Seconds")
# elif a<3600 and a>60:
#     print(str(int(m))+" Minutes "+ str(int(s)) + " Seconds")
# else:
#     print(str(int(s)) + " Seconds")



# string piramid pattern
name = input("Enter you name = ")
string  = name + " "
for i in range(0,len(string)-1):
    for j in range(0,i+1):
        print(string[j], end = " ")
    print(" ")

