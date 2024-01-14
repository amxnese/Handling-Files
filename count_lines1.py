try:
  with open("test.txt",'r') as f:
    lines = f.readlines()
    result = len(lines)
    print(f"Number of Lines in The File is {result} Line")
except FileNotFoundError:
  print("File Not Found")
except Exception as e:
  print(f"An Error Occurred: {e}")