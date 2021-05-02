ascii = 33
for i in range(32):
    coloum1 = f"'{chr(ascii)}'    =O=    {ascii}"
    coloum2 = f"'{chr(ascii+32)}'    =O=    {ascii+32}"
    coloum3 = f"'{chr(ascii+64)}'    =O=    {ascii+64}"
    print(f"|   {coloum1}   |   {coloum2}   |   {coloum3}\t|")
    ascii = ascii+1
