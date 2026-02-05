from time import time

password = input("Enter password (test only): ")
start = time()

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special = "!&$§%/()=?-_"
chars = letters + numbers + special

guesses = 0
found = False

for length in range(1, len(password) + 1):
    combos = ['']
    for _ in range(length):
        combos = [c + ch for c in combos for ch in chars]

    for g in combos:
        guesses += 1
        if g == password:
            found = True
            break

    if found:
        break

print(f"Password cracked: {password}")
print(f"Guesses tried: {guesses}")
print(f"Runtime: {time() - start:.2f} seconds")
