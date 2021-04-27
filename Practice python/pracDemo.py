gender = input("Enter your gender = ")
if gender == "male":
    age = int(input("Enter your age = "))
    if age>=24:
        qualification = input("Enter your qualification = ")
        if qualification == "BE":
            print("Welcome")
        else:
            print("only BE allowed")
    else:
        print("you are younger... not allowed")
else:
    print("only males allowed")