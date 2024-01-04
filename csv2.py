import csv
'writing with regular writer'
with open("new.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file)
    with open("new1.csv","w") as csv1_file:
        csv_writer = csv.writer(csv1_file,delimiter="\t")
        for i in csv_reader:
            csv_writer.writerow(i) 
    'reading with regular reader'
    with open("new1.csv","r") as file1:
        file1_reader = csv.reader(file1,delimiter="\t")
        for i in file1_reader:
            print(i)
    'writing with DictWriter'
    with open("new.csv","r") as file2:
        file2_reader = csv.DictReader(file2)
        with open("new1.csv","w") as file3:
            fieldnames = ['Username','Identifier','First name','Last name']
            file2_writer = csv.DictWriter(file3,fieldnames=fieldnames)
            file2_writer.writeheader()
            for i in file2_reader:
                file2_writer.writerow(i)

    'reading with DictReader'
    with open("new.csv","r") as file2:
        file2_reader = csv.DictReader(file2)
        for i in file2_reader:
            print(i["Identifier"])