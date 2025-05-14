Question_1 = input("What's your favorite animal?: ")
if Question_1 == "cat":
    Answer_1 = "cat"
elif Question_1 == "dog":
    Answer_1 = "dog"
else:
    Answer_1 = "Mysterious"

Question_2 = input("Do you prefer day or night?: ")
if Question_2 == "day":
    Answer_2 = "day"
elif Question_2 == "night":
    Answer_2 = "night"

Question_3 = int(input("Pick a number between 1 and 10: "))
if 1 <= Question_3 <= 5:
    Answer_3 = "low"
else:
    Answer_3 = "high"

print(f"You're a {Answer_1}, {Answer_2}, {Answer_3}")