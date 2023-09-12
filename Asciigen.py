from PIL import Image, ImageDraw, ImageFont


import math

chars = '#№$@B%8&*785&*4_=!{A]}[o0ghjslvnkasdbp+qwertyuifzxc m<~`^:;>-/?"|\/.'

charArray = list(chars)
charsLen = len(charArray)
interval = charsLen/256


scaleFactor = 0.17
charHeight = 18
charWidth = 8


def getChar(InputInt):
    return charArray [math.floor(InputInt * interval)]

text_file = open('output-text.txt', "w")

im = Image.open("Your photo in jpg")

fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(charWidth/charHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB', (charWidth*width, charHeight*height), color = (0, 0, 0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j*charWidth, i*charHeight), getChar(h), font = fnt, fill = (r, g, b))
    text_file.write('\n')


outputImage.save('result.jpg')

outputImage.show()
