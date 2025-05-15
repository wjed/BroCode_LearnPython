age = int(input("Enter your age: "))
if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("This age is invalid")
else:
    print("You are ineligible to sign up. You must be 18+ to sign up")
