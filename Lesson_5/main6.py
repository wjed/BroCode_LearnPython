import math
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
asquared = math.pow(a, 2)
bsquared = math.pow(b, 2)
hypotenuse = math.sqrt(asquared + bsquared)
print(f"The length of the hypotenuse is: {hypotenuse}")