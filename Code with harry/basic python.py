# print('Program Of Addition Of Two Numbers')
# a = int(input('A = '))
# b = int(input('B = '))
# c= a + b
# print(a,'+',b,'=',c)

# comment
# answer = input("Do you want to learn python ?\n")
# if answer == "yes":
#     print("subscribe CodeWithHarry and follow instruction and do pracice")
# else:
#     print("Go To Hell")



# aadi = 'aadesh lokhande aadesh lokhande aadesh lokhande aadesh lokhande'
# print(len(aadi))
# print(aadi[10:])
# print(aadi[:50])
# print(aadi[:])
# print(aadi[::2])



# list = ["aadesh","gautam","lokhande"]
# list[0] = "shubham"
# list.append(".")
# print(list)
# a = list[1]
# print(a)

# p = input("r = ")
# print(p)

# tp = (1,2,1,2,1,2,1,2,1,2,1,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1)
# a= tp.count(2)
# # a = len(tp)
# print(a)




# dict = {"aadesh":"prgrammer", "shubham":"hacher","rahul":"accountant","divya":"kg teacher"}
# a = input("Enter a name = ")
# print(dict[a])
# # print(dict[input("enter your name = ")])





# # greater number(E002 V025)
# a = input("Enter the 1st value = ")
# b = input("Enter the 2nd value = ")
# if a<b:
#     print(b,"is greater.")
# elif a == b:
#     print("Both are same values.")
# else:
#     print(a,"is greater.")




# # If Else
# a = int(input("Enter your age = "))
# if a<100 and a>7:
#     if a>18:
#         print("you can drive.")
#     elif a==18:
#         print("we can't decide. you need to come in office" )
#     else:
#         print("you can't drive")
# else:
#     print("Enter your age currectly")






# # faulty calculator

# a = int(input())
# op = input()
# b = int(input())

# if op == "+":
#     if a == 56 and b == 9:
#         print(a,"+",b,"= 5496")
#     else:
#         c = a + b
#         print(a, "+", b, "=", c)
# elif op == "x":
#     if a == 45 and b == 3:
#         print(a,"X",b,"= 555")
#     else:
#         c = a * b
#         print(a, "x", b, "=", c)

# elif op == "/":
#     if a == 56 and b == 6:
#         print(a,"/",b,"= 4")
#     else:
#         c = a / b
#         print(a, "/", b, "=", c)

# elif op == "-":
#     c = a - b
#     print(c)



# # Enter number continue
# while (True):
#     a = int(input("Enter a value = "))
#     if a<=100:
#         continue
#     else:
#         print("you enter number greate than 100")
#         break



# # # Guess the number v020
#
# # import random
# print("the number is under 100")
# # list = [range(0,100)]
# a = 15
# print()
# # a = 34
# i = 1
# while i<11:
#     num = int(input("Enter the number = "))
#
#     if num ==a:
#         print("You are win, in", i ,"chances")
#         break
#     else:
#         chance = 10 - i
#         if a<num:
#
#             print(num,"is greater than the number.\nyou have",chance,"chance\n")
#
#         else:
#             print(num,"is smaller than the number\nyou have",chance,"chance\n")
#
#     i = i + 1





# a = open("read.txt", "rt")
# line = print(a.readline())
# for line in a:
#     print(line)

# b = a.read()
# print(b)
# for c in a:
#     print(c)
# a.close()




# # write mode
# f = open("read.txt", 'w')
# f.write("chup kr be kutte... soja")
# f.close()
#

# # # append mode
# f = open("read.txt", 'a')
# f.write("\nchup kr be kutte... soja")
# f.close()



# # read and write both
# f = open("read.txt", "r+")
# print(f.read())
# f.write("\naadesh lokhande")


#
# while (True):
#     a = int(input("Enter a value = "))
#     if a<=100:
#         continue
#     else:
#         print("you enter number greater than 100")
#         break



# file creation
# while(True):
#     a = input("Add or Not = ")
#     if a == "add":
#         name = input("Enter File Name = ")
#         msg = input(" Enter your msg = ")
#         write = open((name+".txt"), "a")
#         write.write(msg+ "\n")
#         write.close()
#     elif a=="not":
#         break
#     else:
#         print("invalid input")



# ########### ERROR #############
# name = input("Enter File Name = ")
# write = open((name + ".txt"), "a")
# lines = int(input("How many entries you have = "))
# for lines in range(0, (lines+1)):
#     write.write(msg + "\n")
#     a = int(input(" = "))
#     if lines:
#         msg = input(" Enter your msg = ")
#     elif a=="not":
#         break
#     else:
#         print("invalid input")
#     write.close()





# # # string formatting
# name = input("Enter your Name = ")
# age = int(input("Enter your Age = "))
# print("%s is %s years old"%(name,age))
# a = "{} is {} years old"
# b = a.format(name,age)
# print(b)
# c= f"{name} is {age} years old"
# print(c)





# # join function
# lis = ["Fb", "Insta", "Telegram", "Whatsapp", "Twitter", "Pinintrest"]
# a = " and ".join(lis)
# print(a, "are all social media I used")



# --------------------------MAP------------------------------
# numbers = ["3", "34", "64"]
# numbers = list(map(int, numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1
# print(numbers[2])

# def sq(a):
#     return a*a
#
# num = [2,3,5,6,76,3,3,2]
# square = list(map(sq, num))
# print(square)
# num = [2,3,5,6,76,3,3,2]5
# square = list(map(lambda x: x*x, num))
# print(square)



# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a

# func = [square, cube]
# num = [2,3,5,6,76,3,3,2]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)



# # --------------------------FILTER------------------------------
# list_1 = [1,2,3,4,5,6,7,8,9]

# def is_greater_5(num):
#     return num>5

# gr_than_5 = list(filter(is_greater_5, list_1))
# print(gr_than_5)


# --------------------------REDUCE------------------------------
# from functools import reduce

# list1 = [1, 2, 3, 4, 2]
# num = reduce(lambda x, y: x * y, list1)
# num = 0
# for i in list1:
#     num = num + i
# print(num)





# -----------------Create Class----------------

# # 1
# class Student:
#     pass
#
# aadesh = Student()
# nilesh = Student()
#
# print(aadesh, nilesh)                   # To check they in same memory location or Not
#
# aadesh.surename = "Lokhande"            # Create instance variable. Surname is instance variable
# aadesh.age = 22                                      # Int
# aadesh.mobile = "Honor 8x"                           # String
# aadesh.learn = ["python","C++"]                     # List
# print(f"Aadesh {aadesh.surename}")                  # Print instance variable
# print(aadesh.learn)
#
# nilesh.surename = "Rangari"
# nilesh.age = 19
# print(f"Nilesh age is {nilesh.age}")





# # 2
# class Android:
#     ceo = "sundar pichai"
#     pass
#
# print(Android.ceo)
#
# playstore = Android()
# youtube = Android()
#
# playstore.gameloft = "Asphalt"
# playstore.tencent = "PUBG"
# playstore.glu = "Contract killer"
# print("ceo of playstore is", playstore.ceo)
#
# youtube.bb_ki_vines = "Bhuvan bam"
# youtube.learnex = ["jenny","michelle","Aakash","Myra", "Meera"]
# youtube.wtf = "Alka"
# print("ceo of youtube is",youtube.ceo)
# print(youtube.__dict__)
# Android.ceo = "Larry page"                                          # we can change value of class variable by using class name
# youtube.ceo = "susan"                                               # we can't change value of class variable by using instance variable. it create another instance variable
# print("now youtube ceo is ",youtube.ceo)
# print(youtube.__dict__)






# # -----------------------OOPS-------------------------

# # -------self--------

# # class
# class Boys:
#     live = "amarnagar"
#
#     def printdetails(self):
#         return f"Name is {self.name}. \nHis friend name is {self.fd}. \nHis age is {self.age}. \nHis studying in {self.clg}"
#
#
# nilesh = Boys()
# shubham = Boys()
# aadesh = Boys()
#
# aadesh.name = "Aadesh"
# aadesh.fd = "Tapan"
# aadesh.clg = "Dharampeth science"
# aadesh.age = 22
#
# nilesh.name = "Nilesh"
# nilesh.fd = "aakash"
# nilesh.clg = "aakar clg"
# nilesh.age = 29
#
# shubham.name = "Shuabham"
# shubham.fd = "naresh"
# shubham.clg = "Raisoni"
# shubham.age = 25
#
# # name1 = input("Enter your name = ")
#
#
# print(aadesh.printdetails())








# # ______Constractor_______
#
# class Boys:
#     live = "amarnagar"
#     def __init__(self,aname , afd, aclg, aage):
#         self.name = aname
#         self.fd = afd
#         self.clg = aclg
#         self.age = aage
#
#
#     def printdetails(self):
#         return f"Name is {self.name}. \nHis friend name is {self.fd}. \nHis age is {self.age}. \nHis studying in {self.clg}"
#
#
# nilesh = Boys("Nilesh", "akash","aakar", 19)
# shubham = Boys("Shuabham", "Naresh", "Raisoni",25)
# aadesh = Boys("Aadesh", "Tapan", "Dharampeth", 22)
#
# print(aadesh.printdetails())
#


#
# # ----------OOPS(Constractor)-------------
# class Hero:
#     ind = "Boolywood"
#     def __init__(self,name1,movie1,movie2,movie3,movie4,movie5):
#         self.name = name1
#         self.film1 = movie1
#         self.film2 = movie2
#         self.film3 = movie3
#         self.film4 = movie4
#         self.film5 = movie5
#
#     def printfilm(self):
#         return f"{self.name} in working in {self.ind} and he does {self.film1}, {self.film2}, {self.film3}, {self.film4}, {self.film5}.\n"
#
# srk = Hero("SRK","DDLJ","Kuch kuch hota hai", "Jab tak hai jan", "Badshah","Karan arjun")
# salman = Hero("Salman","Wanted", "Dabang", "Kick", "Karan arjun", "Race 3")
# akshay = Hero("Akshay kumar","Khiladi", "Boss", "Padman", "Houseful", "Hera Fheri")
#
# while True:
#     a = input('Enter Your Fav Actor\'s Name = ')
#     if a == "srk":
#         print(srk.printfilm())
#     elif a == "salman":
#         print(salman.printfilm())
#     elif a == "akshay":
#         print(akshay.printfilm())
#     else:
#         print("invalid Input")
#         break
#




# # -----------------------Class method------------------
# class Employee:
#     no_of_leaves = 10
#
#     def __init__(self, aname, asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"name is {self.name}, salary is {self.salary} and role is {self.role}"
#
#
#     @classmethod
#     def change_leaves(cls,newleaves):                                                   # Class method
#         cls.no_of_leaves = newleaves
#
#
# aadesh = Employee("Aadesh", 205000, "python programmer")
# nilesh = Employee("Nilesh", 568764,"php developer")
#
# aadesh.change_leaves(55)
#
# print(Employee.no_of_leaves)
# print(aadesh.no_of_leaves)
# print(nilesh.no_of_leaves)




# # 2) class method as alternatie constractor
# class Employee:
#     no_of_leaves = 10
#
#     def __init__(self, aname, asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     @classmethod
#     def from_str(cls,string):
#         return cls(*string.split("-"))          #one line
#         # bhula = string.split("-")                     #multiline
#         # return cls(bhula[0], bhula[1],bhula[2])
#
# karan = Employee.from_str("Karan-646543-Worker")
#
# print(karan.salary)





#
# #--------------------------------INHERITANCE------------------------------------
# #
# # Rules :-
# # 1) when a class inherits another class it inherits all features of the parents class.
# # 2) a new child class automatically gets all of the methods and attributes of the existing parents class
#
# # --------CREATE A PARENT CLASS-----------
# # create a class named Person, with firstname and lastname properties, and a printname method:
#
# class  Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#
#     def printname(self):
#         print(f"Hello...!!!, My Name Is {self.firstname} {self.lastname}. He will pass in {self.gra}" )
#
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.gra = year
#         # Person.__init__(self, fname, lname)
# # pass
#
# # x = Person("Aadesh" , "Lokhande")
# # x.printname()
#
# x = Student("Aadesh" , "Lokhande", 2020)
# x.printname()
#





#
# # ----------Diamond shape problem-----------MULTIPLE INHARITANCE-----------------
# class A:
#     def bhula:
#         print("this is A  class")
#     # pass
#
# class B:
#     def bhula:
#         print("this is B class")
#     # pass
#
# class C:
#     def bhula:
#         print("this is C class")
#     # pass
#
# class D:
#     def bhula:
#         print("this is D class")
#     # pass
#
# a = A()
# b = B()
# c= C()
# d = D()
#
# d.bhula()
#





# # # -------------------Dandar methods-----------------
# class Employee:
#     no_of_leaves = 10

#     def __init__(self, aname, asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"name is {self.name}, salary is {self.salary} and role is {self.role}"


#     @classmethod
#     def change_leaves(cls,newleaves):                                                   # Class method
#         cls.no_of_leaves = newleaves

#     def __add__(self, other):
#         return self.salary + other.salary

#     def __truediv__(self, other):
#         return self.salary / other.salary

#     def __repr__(self):
#         return f"Employee('{self.name}',{self.salary},'{self.role}')"

#     def __str__(self):
#         return f"name is {self.name}, salary is {self.salary} and role is {self.role}"

# aadesh = Employee("Aadesh", 100, "python programmer")
# nilesh = Employee("Nilesh", 10,"php developer")

# print(nilesh + aadesh)                              # __add__ method
# print(nilesh / aadesh)                              # __truediv__ method

# # if __str__ in not there so __repr__ will exucate but __str__ is there that time only __str__ method will exucate no matter __repr__ is available or not
# print(aadesh)                                       #__repr__ method or __str__ method

# print(str(nilesh))
# print(repr(nilesh))             #jabtak repr ko kahkar call na kiya jaye tabtak exucate nhi hoga




