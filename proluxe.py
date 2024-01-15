import csv
def create_proluxe_file(product_file_path, proluxe_file_path, threshold_price):
  with open(product_file_path, 'r') as product_file:
    reader = csv.reader(product_file)
    with open(proluxe_file_path, 'w') as proluxe_file:
      writer = csv.writer(proluxe_file)
      for row in reader:
      # Assuming the price is in the third column (index 2)
        try:
          price = float(row[2])
        except ValueError:
          # Skip rows where price is not a valid number
          continue
          if price > threshold_price:
            writer.writerow(row)
# Example usage
create_proluxe_file('products.csv', 'PROLUXE.csv', 100.0)
