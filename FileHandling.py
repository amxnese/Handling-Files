''' Dealing With a File in Reading Mode '''
#Printing out The Content of a txt File
programing = open("programing.txt","r")
content = programing.readlines()
print(content)

# Iterating Through File's Lines
for i in content:
    print(i)

# Checking if The File is Readable
print(programing.readable()) # True

# Closing The File
programing.close()

''' Dealing With a File in Writing Mode '''

# Writing Some Lines into The File, This Step Overrites The Old Content of The File
programing_file = open("programing", "w")
list_of_phrases = ("\nthis is a first line", "\nthis is a second line")
programing_file.writelines(list_of_phrases)

# Passing a Text into The write Method
programing_file.write("Being Something in Process..")
programing_file.close()

''' Dealing With Binary Files '''

# Opening a jpg File in Binary Read Mode. And Copying it in Another jpg File
with open("Tech Addicted.jpg","rb")as pic:
    with open("newpic.jpg","wb") as newpic:
        for i in pic:
            newpic.write(i)

File = open("random.txt") # opened in read mode
print(File.mode) # r
print(File.name) # random.txt
print(File.encoding) # cp65001
print(File.read()) # random.txt Content

from PIL import Image
myImage = Image.open("Tech Addicted.jpg")
myImage.show()
mybox = (300,300,800,800)
MyNewImage = myImage.crop(mybox)
MyNewImage.show()
Myconvertedimage = myImage.convert("L")
Myconvertedimage.show()