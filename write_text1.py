
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
img = Image.open("white.png")
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("arial.ttf",24 , encoding="unic")

text=input("Enter the text: ")
draw.text((img.size[0]/2.8, img.size[1]/2),text,(5,5,5),font=font)
img.save('sample-out-white.png')
