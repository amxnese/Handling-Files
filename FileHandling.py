# programing = open("programing.txt","r")
# print(programing.readlines()[1])
# programing.close()

# for x in programing.readlines():
#     print(x)
# programing.close()

# print(programing.readable())


# programing_file =open("programing","w")
# list_of_phrases = ("\nthis is a first line", "\nthis is a second line")
# programing_file.writelines(list_of_phrases)

# programing.write("Being Something in Process..")
# programing.close()

# with open("Tech Addicted.jpg","rb")as pic:
#     with open("newpic.jpg","wb") as newpic:
#         for i in pic:
#             newpic.write(i)


# import os
# print(os.getcwd())
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.abspath(__file__))


# import os
# print(os.getcwd())
# File = open("random.txt")
# print(File.readlines())
# print(File.mode)
# print(File.name)
# print(File.encoding)
# print(File.read())
# for line in File:
#     print(line)
#     if line.startswith("01"):
#         break
# File.close()


# with open(r"C:\Users\VAIO\amine\fun.txt", "w") as myFile:
    # myFile.write("i just graduated from high school and have no idea what's next")
    # myFile.write("hello from python by pycharm")
    # print(myFile.readline())


# with open(r"C:\Users\VAIO\amine\fun.txt", "r") as myFile:
    # print(myFile.seek(8))
    # print(myFile.read())
    # import os
    # os.remove(r"C:\Users\VAIO\amine\fun.txt")

# from PIL import Image
# myImage = Image.open(r"C:\Users\VAIO\amine\RainbowSkies_Banner.jpg")
# myImage.show()
# mybox = (300,300,800,800)
# MyNewImage = myImage.crop(mybox)
# MyNewImage.show()
# Myconvertedimage = myImage.convert("L")
# Myconvertedimage.show()

# from PIL import Image
# myImage = Image.open(r"C:\Users\VAIO\amine\RainbowSkies_Banner.jpg")
# myConvertedImage = myImage.convert("L")
# myConvertedImage.show("L")

# file_name = None
# tries = 5
# while tries > 0:
#   try:
#     file_name_given = input("please enter the file's name ==>  ").strip()
#     file_name = open(file_name_given,"r")
#     print(file_name.read())
#     break
#   except FileNotFoundError:
#     print("Please Make Sure The Name And Path Given Are Valid")
#     tries -= 1
#     print(f"you have {tries} tries left")
#   except:
#     print("something went wrong, please try again")
#     tries -= 1
#     print(f"you have {tries} tries left")
#   finally:
#     if file_name is not None:
#       file_name.close()
#       print("file closed")
# else:
#     print("you're out of tries")

# f = open("random.txt", "r")
# print(f.read())
# f.close

# with open("random.txt") as f:
#     print(f.read())

# import os
# print(os.getcwd())
# print('#'*50)
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.abspath(__file__))
# file = open("random.txt")

# import csv
# with open("random.csv","r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     with open("new.csv","w") as new_csv_file:
#         fieldnames = ['first name','last name']
#         csv_writer = csv.DictWriter(new_csv_file,fieldnames=fieldnames)
#         csv_writer.writeheader()
#         for line in csv_reader:
#             del line['job']
#             csv_writer.writerow(line)
# import csv
# 'writing with regular writer'
# with open("new.csv","r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     with open("new1.csv","w") as csv1_file:
#         csv_writer = csv.writer(csv1_file,delimiter="\t")
#         for i in csv_reader:
#             csv_writer.writerow(i) 
    # 'reading with regular reader'
    # with open("new1.csv","r") as file1:
    #     file1_reader = csv.reader(file1,delimiter="\t")
    #     for i in file1_reader:
    #         print(i)
    # 'writing with DictWriter'
    # with open("new.csv","r") as file2:
    #     file2_reader = csv.DictReader(file2)
    #     with open("new1.csv","w") as file3:
    #         fieldnames = ['Username','Identifier','First name','Last name']
    #         file2_writer = csv.DictWriter(file3,fieldnames=fieldnames)
    #         file2_writer.writeheader()
    #         for i in file2_reader:
    #             file2_writer.writerow(i)

    # 'reading with DictReader'
    # with open("new.csv","r") as file2:
    #     file2_reader = csv.DictReader(file2)
    #     for i in file2_reader:
    #         print(i["Identifier"])