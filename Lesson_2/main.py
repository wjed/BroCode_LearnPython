# Variable is a container for a value, strings, integers, floats, booleans

#These are strings
first_name = "Will"
favorite_food = "Pizza"
email = "will123@fake.com"

#These are integers
age = 25
quantity = 3
num_of_students = 30

#These are floats

price = 10.99
gpa = 3.98
km = 5.5
is_student = True
is_teacher = False

print(first_name)
print(f"Hello {first_name}")
print(f"You like {favorite_food}")
print(f"Your email is {email}")
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {km} km")
print(f"Are you a student?: {is_student}")

if is_student:
    print("You're a student")
else:
    print("You aren't a student")


for_sale = True

if for_sale:
    print("Item is for sale")
else:
    print("That item is not available")

is_online = False

if is_online:
    print("You're online")
else:
    print("You're offline")