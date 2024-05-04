# Name : Finney Bado
# Date : 03/05/2024
# Description : This program converts a JPEG image into a PNG one


import os
from PIL import Image

# Main body
def jpeg_to_png(path: str) -> None:

    # accessing the folder containing the data
    os.chdir(path)
    pictures = os.listdir(str(os.getcwd()))

    # processing to the format conversion
    for image in pictures:
        if "jpeg" in image:
            im = Image.open(image)
            im.save(image.split(".")[0] + ".png")
            os.remove(image)


jpeg_to_png("/Users/finney/Desktop/JPEG")



