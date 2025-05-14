usersname = str(input("Enter your name: "))
print(f"Hey {usersname}! Thanks for coming to the store. What do you want?")

usersitem = str(input("Enter your item: "))
usersquantity = int(input("Enter your quantity: "))
usersprice = float(input("Enter the price of your item(s): "))
userstotal = usersquantity * usersprice

print("Great Selection!")
print(f"Since you bought {usersquantity} {usersitem}'s and the price for each one was ${usersprice}, " \
f"the total cost would be ${userstotal}")