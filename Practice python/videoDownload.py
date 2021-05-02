# pip install pytube
from pytube import YouTube
# Author = TECH_IN_SECONDS

link = input("Paste URL = ")
vdos = YouTube(link).streams.all()

for vdo in list(enumerate(vdos)):
    print(vdo)

vdos[int(input("Enter Option = "))].download()

name = YouTube(link).title
print(f"\n\nDownload Complete - {name}")