import calendar
date = 20
month = 4
year = 2021
# print(calendar.calendar(year))
# print(calendar.calendar(int(input("Enter Year = "))))

# print(calendar.month(int(input("Enter year = ")),int(input("Enter Month = "))))

# print(calendar.weekday(year,month,date))

# date = calendar.weekday(int(input("Enter year = ")),int(input("Enter Month = ")),int(input("Enter Date = ")))

day =   { 
            0:"Monday",
            1:"Tuesday", 
            2:"Wednesday", 
            3:"Thursday", 
            4:"Friday", 
            5:"Saturday", 
            6:"Sunday"
        }

# print(day[date])
print(day[calendar.weekday(year,month,date)])