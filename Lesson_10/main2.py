# Validate User Input Exercises

username = input("Hello! Enter Your Username: ")
spacecounter = username.count(" ")
if len(username) >= 12:
    print("This Username is Invalid. Please Try Again With Less Than 12 Characters.")
else:
    print("Your Username Passes The Length Check.")

if username.isdigit():
    print("This Username Is Invalid. Please Try Again With Only Letters.")
else:
    print("This USername Passes The Letter Check.")

if spacecounter >= 1:
    print("This Username Is Invalid. Please Try Again With No Spaces.")
else:
    print("This Username Passed The Space Check.")