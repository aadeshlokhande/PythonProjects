# pip install Pillow
from PIL import Image

img = Image.open("ironman.jpg")
black_and_white = img.convert("L")
black_and_white.save("bw_ironman.png")
black_and_white.show()
