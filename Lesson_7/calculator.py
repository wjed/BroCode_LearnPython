operator = input("Enter an operator: ")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    print(round(num1 / num2))
elif operator == "+":
    print(round(num1 + num2), 2)
elif operator == "-":
    result = num1 - num2
    print(f"The first number minus the second number is", round(result, 2))