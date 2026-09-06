# tempconverter.py #

unit = input("Is this temperature in Celsius or Fahrenheit (type C or F): ")
temp = float(input("Enter a temperature: "))

if unit == "C":
    fahrenheit = (temp*(9/5)) + 32
    print(f"That is {fahrenheit}F")
elif unit == "F":
    celcius = round((temp-32)*(5/9), 2)
    print(f"That is {celcius}C")
else:
    print(f"{unit} is invalid, enter C or F kindly.")

