# import calendar
# m = int(input("Enter a Month = "))
# y = int(input("Enter a Year = "))
# try:
#     print("\n",calendar.month(y,m))
# except:
#     print("\nyour Enter Wrong Input")


import webbrowser
url = "https://www.google.com"
if "http" == url[:4]:
    webbrowser.open_new(url=url)
else:
    try:
        url = "https://"+url
        webbrowser.open_new(url=url)
    except:
        url = "http://"+url
        webbrowser.open_new(url=url)

# webbrowser.open_new(url=url)

