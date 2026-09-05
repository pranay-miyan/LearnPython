# weighconvert.py #

import math

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K or L): ")

if unit == "K":
    weight = round(weight * 2.205, 2) 
    unit = "Lbs"
elif unit == "L":
    weight = round(weight / 2.205, 2) 
    unit = "Kg"
else:
    print("Type either (K or L)...")

print(f"Your weight is {weight}{unit}")