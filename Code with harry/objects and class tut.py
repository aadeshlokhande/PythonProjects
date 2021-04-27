# class = templetes
# object = instance of class

# object use DRY(do not repeat yourself) concept

# ---------Creat a first class-----------
class Family():                             # Family is a class
    son = "aadesh"
    pass

lokhande = Family()                         # Lokhande is a object
mendhe = Family()

lokhande.brother = "shuabham"
lokhande.sister = ["aashu", "pragati"]
lokhande.belong = "pappa"

mendhe.brother = "vibhor"
mendhe.sister = "Khushi"
mendhe.belong = "mummy"

print(lokhande.sister)
print(mendhe.son)
print(lokhande.son)
print(Family.son)




