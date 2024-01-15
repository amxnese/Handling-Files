from PIL import Image
myImage = Image.open("Tech Addicted.jpg")
myImage.show()
mybox = (300,300,800,800)
MyNewImage = myImage.crop(mybox)
MyNewImage.show()
Myconvertedimage = myImage.convert("L")
Myconvertedimage.show()