'''
Splitting or partitioning refers to the process of extracting items from a file that possess 
a certain property and organizing them into one or more other file(s).
Let's consider a Product file, where each record consists of the name, code, and price of 
an item.
Write a Python code, starting from the product file, will create the 
PROLUXE file, consisting of all the items from PRODUCT with a price higher than a 
given threshold.
'''

import csv
def proluxe(file_path, output, threshold):
  try:
    with open(file_path, 'r') as f:
      reader = csv.DictReader(f)
      with open(output, 'w',newline='') as out:
        fieldnames = ['Product','Price','Quantity']
        writer = csv.DictWriter(out,fieldnames)
        for line in reader:
          if(float(line["Price"]) > 100):
            writer.writerow(line)

  except FileNotFoundError:
    print("File Not Found")
  except Exception as e:
    print(f"An Error Occurred: {e}")

proluxe("products.csv","PROLUXE1.csv",100)