# pip install stegano
from stegano import lsb

image = "ironman.jpg"
new_img = "data_man.png"

msg = "aadesh lokhande"

# to hide data
lsb.hide(image,message= msg).save(new_img)

# to revel Hidden data
print("Hidden message =", lsb.reveal(new_img))