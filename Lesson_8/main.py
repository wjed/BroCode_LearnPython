weight = int(input("Enter your weight: "))
unit = input("Enter the unit that weight is in (either lbs or kg): ")
if unit == "lbs":
    result = weight * 0.453592
    print(f"Your weight in kilograms is {round(result, 1)}")
elif unit == "kg":
    result = weight * 2.20462
    print(f"Your weight in pounds is {round(result, 1)}")
else:
    print(f'You have not selected a valid unit. Please try again using "lbs" or "kg"')