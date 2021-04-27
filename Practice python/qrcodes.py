#pip install qrcode
import qrcode
# Author = TECH_IN_SECONDS

url = "https://www.instagram.com/tech_in_seconds"
qrcode.make(url).save('qrcode.png')