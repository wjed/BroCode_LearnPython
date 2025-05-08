item = str(input("What item would you like to buy: "))
price = float(input("What's the price of that item: "))
quantity = float(input("So how many of them do you want: "))

total = price * quantity

print(f"Great! You have bought {quantity} {item}'s. Your total for all of that is.. ${round(total, 2)}")