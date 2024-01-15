import csv
' Using csv.reader To Read '
with open("random.csv","r") as csv_file:
    # Creating an Iterable csv.reader Object
    csv_reader = csv.reader(csv_file)

    ' Using csv.writer To Write '
    with open("new.csv","w",newline='') as csv1_file:
        # Creating a csv.writer Object
        csv_writer = csv.writer(csv1_file,delimiter="\t")

        # Iterating over The csv.reader Object
        for line in csv_reader:
            csv_writer.writerow(line) 

' Reading The File That We Created '
with open("new.csv","r") as file:
    file_reader = csv.reader(file,delimiter="\t")
    for line in file_reader:
        print(line)

'Using csv.Dictreader to Read'
with open("users.csv","r") as file:
    # Creating an iterable csv.Dictreader Object
    reader = csv.DictReader(file)

    with open("new_users.csv","w",newline='') as file1:
        fieldnames = ['Username', 'First name', 'Last name']
        writer = csv.DictWriter(file1,fieldnames=fieldnames)
        writer.writeheader()
        for line in reader:
            del line['Identifier']
            writer.writerow(line)

' Specifying What Key To Print '
with open("users.csv","r") as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line["Identifier"])