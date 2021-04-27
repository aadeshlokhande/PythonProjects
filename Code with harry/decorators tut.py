# #--------------------------------
# def function1():
#     print("Subscribe now")
#
# function2 = function1
# del function1
# function2()
####################################


# #----- function in function------
# def func(num):
#     if num==1:
#         return int
#     if num==0:
#         return print
#
# a = func(0)
# print(a)
###################################



# #--------------------------------
# def executor(func):
#     func("Aadesh")
#
# executor(print)
###################################



# #------------decorator------------
def dec1(func1):
    def nowrun():
        print("Aadesh")
        func1()
        print("Lokhande")
    return nowrun

@dec1                           # line 41
def mname():
    print("Gautam")

# mname = dec1(mname)           # line 41 and 45 are same
mname()


















