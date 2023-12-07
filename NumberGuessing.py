import random

user_number = input("Type a number: ")

if user_number.isdigit():
    user_number =int(user_number)

    if user_number < 0:
        print("Type a number larger than 0.")
        quit()
else:
    print("Please type only number next time.")
    quit()

random_number = random.randint(1, user_number)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess =int(user_guess)
    else:
        print("Please type only number next time.")
        continue

    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess < random_number:
        print("You were below the number.")
    else:
        print("You were above the number.")

print(f"You got it in {guess} guesses!")
