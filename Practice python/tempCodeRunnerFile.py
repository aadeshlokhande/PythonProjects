# # pip install ascii_magic
# import ascii_magic
# # Author = TECH_IN_SECONDS

# output = ascii_magic.from_image_file("python.jpg", columns=60, char = "#")
# ascii_magic.to_terminal(output)


# # creating variables
# a, b, c = 70,80,90
# # printing value of variables
# print('a :',a)
# # OUTPUT = a : 70
# print('b :',b)
# # OUTPUT = b : 80
# print('c :',c)
# # OUTPUT = c : 90

# # Function definition
# def add():
#     # Creating Variable
#     x= 50
#     y = 30
#     z = x + y
#     print("Add = ", z)
# # Calling Fuctn
# add()
# # OUTPUT = 80
# # this line will raise an error Bcoz x is local variable and it  can't be accessed outside fuction
# print(x)
# # OUTPUT = NameError: name 'x' is not defined


# Creating global variable
x = 50
y = 30
def add():
    # accessing global variable
    # inside a function
    print("Inside funtion Sum = ", x+y)
# Calling function
add()
# Outside a funtion
print("Outside function Sum = ", x+y)
"""
****OUTPUT****
Inside funtion Sum = 80
Outside function Sum = 80
"""