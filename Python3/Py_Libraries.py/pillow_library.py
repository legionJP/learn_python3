from PIL import Image , ImageFilter

image1 = Image.open('image.png')
image1.show()

#jpg to png 
#image1.save('image.png')

#converting image png to jpg 
with Image.open("image.png") as im:
    #  Set the mode to RGB
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
        i.save('pngs/{}.png'.format(fn)) #converting images to pngs


# Resizing the files 

size_300 = (300, 300)
size_700 =(700,550) # for 700 pixels image
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        # print(fn)
        # print(fext)
        i.thumbnail(size_300) #takes size in tuples
        i.save('pngs/{}_300{}'.format(fn,fext)) #fn is filename_300.jpg(fext)

        i.thumbnail(size_700) #takes size in tuples
        i.save('pngs/{}_700{}'.format(fn,fext))


#Roatate the iage

image2 = Image.open('sachitanand_sign.jpg')
image2.rotate(90).save('image90.jpg')

#to convert in the BW image
image2.convert(mode='L')
image2.show()            

#Blur the image  , by Imagefilter
image2.filter(ImageFilter.GaussianBlur(15))
image2.show()
