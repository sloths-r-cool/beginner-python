import random

username = input("Enter a user: (2-8 chars) ")
while len(username) < 2 or len(username) > 8:
    print("2-8 characters please.")
    username = input("Enter a username: ")

def game_instructions():
    print("Each round, you will have 2 choices.")
    print("Each choice has its own action and respected consequence.")
    print("One will either be safe, or one may take away health.")
    print("Good luck.")

game_instructions()

health = 100
rounds_survived = 0

def round():
    global health, rounds_survived

    trap_number = random.randint(1, 2)
    print(f"\nHealth: {health}")
    print("Pick a number: 1 or 2")
    choice = int(input("> "))

    if choice == trap_number:
        damage = random.randint(5, 20)
        health -= damage
        print(f"Wrong, {username}!You took {damage} damage. Health: {health}")
    else:
        print("Lucky! You move to the next round.")

    rounds_survived += 1
    print(f"You have survived round {rounds_survived}")

while health > 0:
    round()

print(f"You have died! You got up to round {rounds_survived}")

if rounds_survived <= 5:
    print(f"You might be the unluckiest person {username}..")
elif rounds_survived <= 10:
    print(f"Unlucky {username}!")
elif rounds_survived <= 20:
    print(f"Oof, that was an alright run {username}!")
elif rounds_survived <= 30:
    print(f"Wow! Nice run {username}!")
else:
    print(f"You got so lucky {username}..")

