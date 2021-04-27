from instapy import client

username = 'Your username'
password = 'your password'

image = 'insta.jpg'

comment = 'Auto Post..'+ '\r\n' + 'Coded By : @aadesh_lokhande'

with client(username, password) as cli:
    cli.upload(image, comment)