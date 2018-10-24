from PIL import Image

img = Image.open("beach.jpg")
#img.show() # original image

pixmap = img.load()

#print(type(pixmap[100,100]))\#tuple
 
r, g, b = pixmap[100,100] #unpacking a tuple, if you know how many elements are inside the tuple
 
 
for i in range(img.size[0]):
    for j in range(0,img.size[1]):
        r, g, b = pixmap[i,j]
        r += i
        g += i
        b += i
        pixmap[i,j] = (r, g, b)

img.show()