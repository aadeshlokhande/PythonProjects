import os
# Author = TECH_IN_SECONDS

path = r'/media/aadesh/Data/Aadesh Lokhande/1 Study Material/stock market'

for filename in os.listdir(path):
    a = filename.split()
    b = a[1]+a[2]
    # os.rename(path+ "/" + filename, path + '/' + b)
    print(b)
