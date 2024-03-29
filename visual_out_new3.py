



from PIL import Image
import PIL.ImageOps    

import sys
infile1 = Image.open('sample-out-white.png_share1.png')
infile1_pixel = infile1.load()
infile2 = Image.open('sample-out-white.png_share2.png')
infile2_pixel = infile2.load()
outfile = Image.new('1', infile1.size)
outfile_pixel = outfile.load()
    
for x in range(infile1.size[0]):
    for y in range(infile1.size[1]):
        if (infile1_pixel[x,y] == infile2_pixel[x,y]):
            outfile_pixel[x,y] = 1
        else:
            outfile_pixel[x,y] = 0
    
def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)

change_contrast(outfile, 900)

inverted_image = outfile.convert('L')
inverted_image = PIL.ImageOps.invert(inverted_image)
inverted_image = inverted_image.convert('1')
change_contrast(inverted_image, 900)
inverted_image.save("new.png")
