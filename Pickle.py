import pickle

class Laptop:
  def __init__(self, model:str, cpu:str, price:float):
    self.model = model
    self.cpu = cpu
    self.price = price

  def describe(self):
    print(f"{self.model} with a {self.cpu} cpu and a price of ${self.price}")

laptop1 = Laptop("Thinkpad", "i511", 299.99)
laptop2 = Laptop("HP", "i510", 199.99)
laptop3 = Laptop("AZUZ", "i710", 219.99)
laptop1.describe()

' Dumping '
with open("laptop.pickle", 'wb') as f:
  pickle.dump(laptop1, f)
  pickle.dump(laptop2, f)
  pickle.dump(laptop3, f)

' Loading '
with open("laptop.pickle", 'rb') as f:
  lst = []
  while True:
    try:
      lst.append(pickle.load(f))
    except EOFError:
      break

for laptop in lst:
  laptop.describe()