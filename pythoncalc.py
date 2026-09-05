# pythoncal.py #

import math

# 1) input numbers, 2) input symbols, 3)input numb 2 4) print ans

usernum1 = float(input("What is your first number?: "))
symbols = input("What is your operator? (+ - * /): ")
usernum2 = float(input("What is your second number?: "))

if symbols == "+":
    result = round(usernum1+usernum2, 2)


    print(f"The answer is {result}") 
elif symbols == "-":
    result = round(usernum1-usernum2, 2)


    print(f"The answer is {result}") 
elif symbols == "/":
    result = round(usernum1/usernum2, 2)


    print(f"The answer is {result}") 
elif symbols == "*":
    result = round(usernum1*usernum2, 2)


    print(f"The answer is {result}") 
else:
    print(f"{symbols} is not valid")

