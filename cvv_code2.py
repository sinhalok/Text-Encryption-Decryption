
import random

from PIL import Image
def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)

def two_of_two(filename):
    """Generates a (2,2) visual cryptography scheme."""
    original = change_contrast(Image.open(filename), 900)
    original = original.convert("1")
    o_pixels = original.load()
    
    first = Image.new("1", (original.size[0] , original.size[1] * 2))
    f_pixels = first.load()
    
    second = Image.new("1", (original.size[0], original.size[1] * 2))
    s_pixels = second.load()
    
    for i in range(original.size[0]):
        for j in range(original.size[1]):
            if o_pixels[i,j] == 0:
                if random.randint(0, 1):
                    f_pixels[i,j * 2    ] = 1
                    f_pixels[i,j * 2 + 1] = 0
                    s_pixels[i,j * 2    ] = 0
                    s_pixels[i,j * 2 + 1] = 1
                else:
                    f_pixels[i,j * 2    ] = 0
                    f_pixels[i,j * 2 + 1] = 1
                    s_pixels[i,j * 2    ] = 1
                    s_pixels[i,j * 2 + 1] = 0
            else:
                if random.randint(0, 1):
                    f_pixels[i,j * 2    ] = 0
                    f_pixels[i,j * 2 + 1] = 1
                    s_pixels[i,j * 2    ] = 0
                    s_pixels[i,j * 2 + 1] = 1
                else:
                    f_pixels[i,j * 2    ] = 1
                    f_pixels[i,j * 2 + 1] = 0
                    s_pixels[i,j * 2    ] = 1
                    s_pixels[i,j * 2 + 1] = 0
    
    first.save(filename + "_share1.png")
    second.save(filename + "_share2.png")
    

if __name__ == '__main__':
    two_of_two("sample-out-white.png")
