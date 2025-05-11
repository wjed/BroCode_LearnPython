import math

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"The circumference of the circle is: {round(circumference, 2)}")
print(f"The area of the circle is: {area}")
# This code calculates the circumference and area of a circle given its radius.