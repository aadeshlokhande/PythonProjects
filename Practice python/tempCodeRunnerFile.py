# pip install ascii_magic
import ascii_magic
# Author = TECH_IN_SECONDS

output = ascii_magic.from_image_file("python.jpg", columns=60, char = "#")
ascii_magic.to_terminal(output)