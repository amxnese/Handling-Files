import json
class Car:
  def __init__(self, model:str, price:float):
    self.model = model
    self.price = price
  
  def describe(self):
    print(self.model, self.price, sep=" : ")

car1 = Car("mustang", 30000)
car1.describe()

' Dumping '
with open("ford.json", 'w') as f:
  data = {"model" : car1.model, "price" : car1.price}
  json.dump(data, f)

' Loading '
with open("ford.json", 'r') as f:
  content = json.load(f)

car2 = Car(content["model"], content["price"])
car2.describe()