#!/usr/bin/env python3.8

import math
import sys

#-------------------------------------------------------
# Exception Argument
try:
    assert len(sys.argv) == 2
except AssertionError:
    print("\n[!] Sorry, This Script need (only) 1 File or Path as Parameter")
    print("\n[!] TRY: [script_name.py] [file_name]\n")
    exit()

#-------------------------------------------------------
# Open FIle Exception
# 'r' open for reading (default)
# 'b' binary mode
try:
    f = open(sys.argv[1], "rb")
except FileNotFoundError:
    print("\n[!] Sorry, File or Path not Found")
    exit()

# Read File
bmp_17_DATA = []
bmp_17_DATA = f.read()

#Close
f.close

#-------------------------------------------------------

a_02 = []
for i in range(0, len(bmp_17_DATA)): a_02.append(bmp_17_DATA[i])

bmp_17_DATA = []
for i in a_02: bmp_17_DATA.append(i.to_bytes(1, byteorder='little').hex())

#-------------------------------------------------------

for i in range(54): bmp_17_DATA.pop(0)

while bmp_17_DATA[len(bmp_17_DATA)-1] == '00': bmp_17_DATA.pop()

#-------------------------------------------------------

hex_list = []

hex_list.extend(bmp_17_DATA)

final_list = []

for i in hex_list: final_list.append(int(i, 16))

# -------------------------------------------------------
# Open FIle

new_file_name = "new_decoded_file"

# 'x' open for exclusive creation, failing if the file already exists
# 'b' binary mode
# Exception Argument
try:
    f = open(new_file_name, "xb")
except FileExistsError:
    print("\n[!] Sorry, File already Exists")
    print("\n[!] Try Rename the File [", new_file_name,"] or Change the Path\n")
    exit()

for i in final_list: f.write(bytes([i]))

f.close
