import random

logo = '''

 _____ _     _____ ____  ____    _____ _     _____   _      _     _      ____  _____ ____ 
/  __// \ /\/  __// ___\/ ___\  /__ __Y \ /|/  __/  / \  /|/ \ /\/ \__/|/  __\/  __//  __\
| |  _| | |||  \  |    \|    \    / \ | |_|||  \    | |\ ||| | ||| |\/||| | //|  \  |  \/|
| |_//| \_/||  /_ \___ |\___ |    | | | | |||  /_   | | \||| \_/|| |  ||| |_\\|  /_ |    /
\____\\____/\____\\____/\____/    \_/ \_/ \|\____\  \_/  \|\____/\_/  \|\____/\____\\_/\_\


'''

print(logo)

def easy():
    secret = random.randint(1, 100)
    attempts = 10
    print(f"You have {attempts} attempts to guess the number.")

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess == secret:
            print(f"🎉 You got it! The number was {secret}.")
            return
        elif guess < secret:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts left.")
        else:
            print(f"❌ Sorry, you're out of attempts. The number was {secret}.")

def hard():
    secret = random.randint(1, 100)
    attempts = 5
    print(f"You have {attempts} attempts to guess the number.")

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess == secret:
            print(f"🎉 CONGRATS! You guessed it right, the number was {secret}.")
            return
        elif guess < secret:
            print("Too Low, Try again.")
        else:
            print("Too High, Try again.")

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts left.")
        else:
            print(f"❌ Sorry, you're out of attempts. The number was {secret}.")

print("I'm thinking of a number between 1 and 100.")
last = random.randint(1, 100)
print(f"The Last Time Guessed number is {last}")
level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()

if level == "easy":
    easy()
elif level == "hard":
    hard()
else:
    print("Invalid choice.")
