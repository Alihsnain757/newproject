from unicodedata import name


l1 = ["Harry", "Sohail","Sahil", "Ahmad"]

if name in l1:
    if name.startswith("S"):
          print("Hello" + name)