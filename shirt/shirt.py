import sys
from PIL import Image, ImageOps
import os

def check():
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >3:
        sys.exit("Too many command-line arguments ")
    else:
        root1, ext1 = os.path.splitext(sys.argv[1])
        root2, ext2 = os.path.splitext(sys.argv[2])
        formats = [".jpg", ".png", ".jpeg"]
        if ext1 in formats:
            if ext2 in formats:
                if ext1 == ext2:
                    image(sys.argv[1],sys.argv[2])
                else:
                    sys.exit("Input and output have different extensions")
            else:
                sys.exit("Invalid output")
        else:
            sys.exit("Invalid input")

def image(p1,p2):
    try:
        b_pic = Image.open(p1)
        shirt = Image.open("shirt.png")
        w,h = shirt.size
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        b_pic = ImageOps.fit(b_pic, (w,h))
        b_pic.paste(shirt,shirt)
        b_pic.save(p2)

check()

