import ascii_magic
print("\n\n\n")
output = ascii_magic.from_image_file("python.jpg", columns=60, char = "#")
print(output)
print("\n\n\n")



# for leaf in [*range(10)] + [2]: print(f'{"X"*(leaf*2+1):^30}')