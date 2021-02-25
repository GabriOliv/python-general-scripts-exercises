#!/usr/bin/env python3.8

import math
import sys

#-------------------------------------------------------

# Transform Int to a Strings List of Hexadecimal
# EX: 16 --> (0x10) --> ["10","00"]
def int_to_hex_list(int_entry, out_size, endian):
    #Int to Hex in List

    if endian == 1:
        int_entry = int_entry.to_bytes(out_size, byteorder='big')
    elif endian == 0:
        int_entry = int_entry.to_bytes(out_size, byteorder='little')
        
    int_entry = int_entry.hex()

    bits_pixel = []
    for i in range(0, len(int_entry), 2): bits_pixel.append(int_entry[i:i+2])

    return bits_pixel

#-------------------------------------------------------
# OPEN USER DATA

# Argument Count
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

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
aux = []
aux = f.read()

#Close
f.close

#-------------------------------------------------------

bmp_17_DATA = []
for i in aux: bmp_17_DATA.append(i.to_bytes(1, byteorder='little').hex())

#-------------------------------------------------------
# BMP FILE STRUCTURE
#-------------------------------------------------------
# bmp_01_FileType = ["42","4D"]
# bmp_02_FileSize = ["00","00","00","00"]
# bmp_03_01_Reserved = ["00","00"]
# bmp_04_02_Reserved = ["00","00"]
# bmp_05_PixelDataOffset = ["36","00","00","00"]
# bmp_06_HeaderSize = ["28","00","00","00"]
# bmp_07_ImageWidth    length = 4 EX: ["05","00","00","00"]
# bmp_08_ImageHeight    length = 4 EX: ["05","00","00","00"]
# bmp_09_Planes = ["01","00"]
# bmp_10_BitsPerPixel    length = 2 EX: ['10', '00']
# bmp_11_Compression = ["00","00","00","00"]
# bmp_12_ImageSize = ["00","00","00","00"]
# bmp_13_XpixelsPerMeter = ["00","00","00","00"]
# bmp_14_YpixelsPerMeter = ["00","00","00","00"]
# bmp_15_TotalColors = ["00","00","00","00"]
# bmp_16_ImportantColors = ["00","00","00","00"]
# bmp_17_DATA length = -- EX: ["FF","7F","00","00","FF","7F","00"]

#-------------------------------------------------------
# BMP FILE STRUCTURE [Header Fill]
bmp_01_FileType = int_to_hex_list(16973, 2, 1)
bmp_02_FileSize = int_to_hex_list(0, 4, 0)
bmp_03_01_Reserved = int_to_hex_list(0, 2, 0)
bmp_04_02_Reserved = bmp_03_01_Reserved
bmp_05_PixelDataOffset = int_to_hex_list(54, 4, 0)
bmp_06_HeaderSize =  int_to_hex_list(40, 4, 0)
bmp_09_Planes = int_to_hex_list(1, 2, 0)
bmp_11_Compression = bmp_02_FileSize
bmp_12_ImageSize = bmp_02_FileSize
bmp_13_XpixelsPerMeter = bmp_02_FileSize
bmp_14_YpixelsPerMeter = bmp_02_FileSize
bmp_15_TotalColors = bmp_02_FileSize
bmp_16_ImportantColors = bmp_02_FileSize

#-------------------------------------------------------
# VARIABLES TO SCRIPT
#Choose
#   BitperPixel for 16(0x10)
#   BitperPixel for 24(0x18)
#   BitperPixel for 32(0x20)
bitsperpixel = 32

bmp_10_BitsPerPixel = int_to_hex_list(16, 2, 0)
print("\nBits per Pixel:", bitsperpixel, bmp_10_BitsPerPixel)

# len of user data
data_size = len(bmp_17_DATA)
# divisor of bytes per pixel
#   2 se BitperPixel for 16(0x10)
#   3 se BitperPixel for 24(0x18)
#   4 se BitperPixel for 32(0x20)
divisor = bitsperpixel / 8

image_square_dim = math.ceil( math.sqrt( data_size/divisor ))

new_data_size = int((image_square_dim**2)*divisor)

extra_data_size = int(new_data_size - data_size)

print("User Data Length:", data_size)
print("Square Dimension:", image_square_dim)
print("New Data Size:", new_data_size)
print("Null Complementary Data :", extra_data_size)

bmp_07_ImageWidth = int_to_hex_list(image_square_dim, 4, 0)
bmp_08_ImageHeight = int_to_hex_list(image_square_dim, 4, 0)

#-------------------------------------------------------
# BMP FILE STRUCTURE [Data Fill]
hex_list = []

hex_list.extend(bmp_01_FileType)
hex_list.extend(bmp_02_FileSize)
hex_list.extend(bmp_03_01_Reserved)
hex_list.extend(bmp_04_02_Reserved)
hex_list.extend(bmp_05_PixelDataOffset)
hex_list.extend(bmp_06_HeaderSize)
hex_list.extend(bmp_07_ImageWidth)
hex_list.extend(bmp_08_ImageHeight)
hex_list.extend(bmp_09_Planes)
hex_list.extend(bmp_10_BitsPerPixel)
hex_list.extend(bmp_11_Compression)
hex_list.extend(bmp_12_ImageSize)
hex_list.extend(bmp_13_XpixelsPerMeter)
hex_list.extend(bmp_14_YpixelsPerMeter)
hex_list.extend(bmp_15_TotalColors)
hex_list.extend(bmp_16_ImportantColors)

hex_list.extend(bmp_17_DATA)

#NULL DATA ADD
for i in range(extra_data_size): hex_list.append("00")

# -------------------------------------------------------

final_list = []

for i in hex_list: final_list.append(int(i, 16))

# -------------------------------------------------------
# Open FIle

new_file_name = "new_encoded_img.bmp"

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

