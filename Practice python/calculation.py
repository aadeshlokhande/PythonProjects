# https://www.geeksforgeeks.org/powerful-one-liner-python-codes/
# print("Result = ", eval(input("Enter The Expression = ")))
# print ('\n'.join(line.split(":",1)[0] for line in open("/etc/passwd")))
# print('\n'.join("%i Byte = %i Bit = largest number: %i" % (j, j*8, 256**j-1) for j in (1 << i for i in range(8))))

# import functools
# print(functools.reduce(lambda x, y: x * y, range(1, 5 + 1)))

# # 1) Calculator
# Equation = input("Enter a Equation = ")
# Answer = eval(Equation)
# print("Answer = ", Answer)

# 2) One Liner Calculator
print("Answer = ", eval(input("Enter a Equation = ")))