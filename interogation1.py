with open("af.txt",'r') as f1:
  with open("tst.txt",'r') as f2:
    num1 = f1.read()
    num2 = f2.read()
    result = int(num1) + int(num2)
print(result)