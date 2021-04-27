from prettytable import PrettyTable

myTable = PrettyTable(["Name", "User", "following", "Followers"])

myTable.add_row(["Aadesh", "23", "7058232826", "aadeshlokhande11@gmail.com"])
myTable.add_row(["Rohit", "34", "6785764533", "rohit31@gmail.com"])
myTable.add_row(["Sudhir", "54", "8674563455", "sudhir45@gmail.com"])
myTable.add_row(["Nilesh", "12", "4636345366", "nilesh34@gmail.com"])
myTable.add_row(["Shubham", "34", "1233455666", "shubham56@gmail.com"])

print(myTable)