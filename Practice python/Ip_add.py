import socket

url = "google.com"          # changable string
print(f"Ip Address of {url} is {socket.gethostbyname(url)}")
