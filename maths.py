import math


# friends = 0

# # #augument assign operator
# # friends += 1

# # friends -= 2

# # friends *= 3

# # friends /= 2

# # friends **= 2

# # friends %= 2

# # remainder = friends 

# print(friends)


# x = 3.1415
# y = 4
# z = 5

# # result = round(x)
# # result = abs(y) # abs = distance away from 0 thus 4 away, cuz -4+4 = 0 
# # result = pow(y, 3) #(power off)
# # result = max(x,y,z) max value of all
# # result = min(x,y,z) min value of all

# print(result)

# print(math.pi) for pi
# print(math.e) for eulers number

# x = 9.1

# # result = math.sqrt(x) squareroot 
# # result = math.ceil(x) rounds up, eg 9.1 to 10
# # result = maths.floor(x) rounds down eg 9.9 to 9


# print(result)


# exercise maths 1 - circumference of circle

# radius = float(input("What is the radius of the circle?: "))
# circumference = radius * 2 * math.pi

# print(f"The circumference of the circle is {round(circumference, 2)}cm")

# excercise 2 - area of the circle

# radius = float(input("What is the radius of the circle?: "))

# area = math.pi * pow(radius , 2)

# print(f"The area of the cirlce is {round(area, 2)}cm")

# excerise 3 - hypotneus of triangle

a = float(input("What is the base  of the triangle?: "))
b = float(input("What is the  height of the triangle?: "))
tArea = math.sqrt(pow(a,2)+ pow(b, 2))


print(f"Area of the triangle is {round(tArea, 2)}cm")