import random

def play_game():
    number = random.randint(1, 20)
    attempts = 0

    print("Guess the number (1–20)")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f" Correct! You took {attempts} tries.")
            break


while True:
    play_game()

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Bye!")
        break