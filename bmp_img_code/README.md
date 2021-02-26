# bmp_img_code

[![Python Version](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/)

-----


## Overview
Script to Convert Files (like .zip or .txt) to Bitmap Images

## How to Use

##### Encode a file to Bitmap Image:
* Input: **file.zip**
    ```
    python3.8 bmp_encode.py file.zip
    ```

* Output: **new_encoded_img.bmp**

##### Decode Bitmap Image to original File:

* Input Example: **new_encoded_img.bmp**
    ```
    python3.8 bmp_encode.py new_encoded_img.bmp
    ```

* Output: **new_decoded_file**

<p align="center">
    <img src="https://raw.githubusercontent.com/GabriOliv/python-general-scripts-exercises/main/bmp_img_code/img_share.svg" alt="drawing" width="300">
</p>


## Warnings and Cautions 

* The Encode script have the BitperPixel set on 32(0x20), so to convert back from another format (.png, .tiff, ...) use a Bitmap 32bits Convertor, or change the BitperPixel value;
* The Encoder and Decoder just add and remove the Bitmap Header and some 0x00 bits, without compression or encryption. If you want more security, just encrypt the original file with other methods before use this script, so the image can be safely shared;
* Try use only Lossless Compression Image types to share, prevents the corruption of the original file.
