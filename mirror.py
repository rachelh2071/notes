from PIL import Image
from random import randint


def left_mirror(img):
    pixmap = img.load()
    for i in range(img.size[0]//2):
        for j in range(img.size[1]):
            pixmap[i,j] = pixmap[img.size[0]-1-i,j]
    img.show()

def bottom_mirror(img):
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]//2):
            pixmap[i,j] = pixmap[i,img.size[1]-1-j]
    img.show()
    
def major_mirror(img):
    img.show()
    pixmap = img.load()
    for i in range(img.size[1]):
        for j in range(img.size[1]):
            pixmap[i,j] = pixmap[j,i]
    img.show()

def minor_mirror(img):
    img.show()
    pixmap = img.load()
    wmid = img.size[0]//2
    hmid = img.size[0]//2
    for i in range(img.size[1]):
        for j in range(img.size[1]):
            pixmap[i,j] = pixmap[img.size[1]-1-j,img.size[1]-1-i]
    img.show()

            
def main():
    img = Image.open("beach.jpg")
    minor_mirror(img)

if __name__ == "__main__":
    main()
        
 