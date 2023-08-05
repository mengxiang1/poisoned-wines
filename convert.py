#converts formats to hex

import re

val = input("Input value: ")
val_arr = val.split(" ")
if len(re.findall(r"[A-Z\s]+", val)) == 1:
    digits = ord(max(val)) - 65
    val_arr = [[digits - (ord(j) - 65) for j in i] for i in val_arr]
    hex_arr = []
    for i in val_arr:
        temp = ["0"] * (digits + 1)
        for j in i:
            temp[j] = "1"
        print(temp)
        hex_arr.append(hex(int("".join(temp), 2))[2:])
    print(val_arr)
    print(" ".join(hex_arr))
else:
    print(" ".join([hex(int(i, 2))[2:] for i in val_arr]))