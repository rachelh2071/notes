from PIL import Image
from random import randint

def filter1(img_name):
    img = Image.open(img_name)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(0,img.size[1]):
            r, g, b = pixmap[i,j]
            r -= j//2
            g -= j//2
            b -= j//2
            pixmap[i,j] = (r, g, b)
    img.show()
    img.save("filter2.jpg")

def filter2(img_name): #g,b,b
    img = Image.open(img_name)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(0,img.size[1]):
            r, g, b = pixmap[i,j]
            num = 255
            pixmap[i,j] = (num-r,num-g,num-b)
    img.show()
    img.save("filter1.jpg")
    
def filter3(img_name): #g,b,b
    img = Image.open(img_name)
    pixmap = img.load()
    for i in range(img.size[0]):
        for j in range(0,img.size[1]):
            r, g, b = pixmap[i,j]
            pixmap[i,j] = (g,b,b)
    img.show()
    img.save("filter3.jpg")
    
def main():
    filter3("beach.jpg")
    
if __name__ == "__main__":
    main()