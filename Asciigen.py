from PIL import Image, ImageDraw, ImageFont


import math

chars = '#№$@B%8&*785&*4_=!{A]}[o0ghjslvnkasdbp+qwertyuifzxc m<~`^:;>-/?"|\/.'

charArray = list(chars)
charsLen = len(charArray)
interval = charsLen/256

print(charsLen)

text_file = open('output-text.txt', "w")

def getChar(InputInt):
    return charArray [math.floor(InputInt * interval)]

# im = Image.open('Your photo')

scaleFactor = 0.2
charHeight = 18
charWidth = 8
width, height = im.size

fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)


im = im.resize((int(scaleFactor*width*(charWidth/charHeight)), int(scaleFactor*height)), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new( mode = 'RGB', size = (charWidth*height, charHeight*width), color = (10, 10, 10))

d = ImageDraw.Draw(outputImage)

for i in range(width):
    for j in range(height):
        r,g,b = pix[i,j]
        h = int(r/3 + g/3 + b/3)
        pix[i, j] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j*charWidth, i*charHeight), getChar(h), font = fnt, fill = (r, g, b))
    text_file.write('\n')


#outputImage.save('result.jpg')

#outputImage.show()