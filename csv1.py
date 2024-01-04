import csv
with open("random.csv","r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open("new.csv","w") as new_csv_file:
        fieldnames = ['first name','last name']
        csv_writer = csv.DictWriter(new_csv_file,fieldnames=fieldnames)
        csv_writer.writeheader()
        for line in csv_reader:
            del line['job']
            csv_writer.writerow(line)