def CountAll(string):
    lower = 0
    upper = 0
    number = 0
    symbol = 0
    for char in string:
        if char.islower():
            lower = lower + 1
        elif char.isupper():
            upper = upper + 1
        elif char.isdigit():
            number = number+ 1
        else:
            symbol = symbol + 1

    return {"lower":lower, "upper":upper,"number":number, "symbol":symbol}
    

a = CountAll("Aadesh@123")
print(a["upper"])
