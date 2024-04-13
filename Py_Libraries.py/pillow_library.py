from PIL import Image

image1 = Image.open('image.png')
image1.show()

#jpg to png 
#image1.save('image.png')

#converting image png to jpg 
with Image.open("image.png") as im:
    # ✅ Set the mode to RGB
    rgb_im = im.convert('RGB')
    rgb_im.save('image1.jpg')

import os 

#opening the fies with the same extensions and converting them into jpeg

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, text = os.path.splitext(f)
        # print(fn)
        # print(text)
        i.save('pngs/{}.png'.format(fn))


# Resizing the files 
