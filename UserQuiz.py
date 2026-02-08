firstname = input("What is your name?")
lastname = input("What is your last name?")
age = input("How old are you?")
# These inputs will determine factors for setting the username

firstnamesub = firstname[:3]
lastnamesub = lastname[:3]

username = firstnamesub + lastnamesub + age

print("Welcome, " + firstname + ". Your username is " + str(username))

score = 0

print(str(username) + ", you will be answering 5 questions.")
print("You will be marked out of 5")
print("First question…")
# question 1
print("What is your name?")
answer = input()
if answer.lower() != firstname.lower():
    print("Wrong, you literally got your name wrong.")
    print("Your score is ", score, username)
    print("Next question:")
else:
    score += 1
    print("Correct ", username + ". Your score is ", score)
    print("Next question:")
# question 2   
print("What is 6*7/42 ?")
answer = input()
if answer == "1":
    score += 1
    print("Correct ", username + ". Your score is ", score)
    print("Next question:")
else:
    print("Incorrect ", username + ". Your score is ", score)
    print("Next question:")
#question 3
print("How many years is a decade?")
answer = input()
if answer == "10":
    score += 1
    print("Correct ", username + ". Your score is ", score)
    print("Next question:")
else:
    print("Incorrect ", username + ". Your score is ", score)
# question 4
try:
    answer = int(input("I have 263 apples. I eat 63 and then half the rest. How many apples do I have left? "))
    if answer == 100:
        score += 1
        print("Correct ", username + ". Your score is ", score)
        print("Next question:")
    else:
        print("Incorrect, ",username +". Your score is ",score)
        print("Next question:")
except ValueError:
        print("Please enter a valid number.")
# question 5
answer = float(input("What is 7*9/2+3-1*0"))
if answer == 34.5:
    score += 1
    print("Correct.")
    print(username, ". Your final score was ",score)
else:
    print("Incorrect.")
    print(username, ". Your final score was ",score)

if score <=2:
    print("You scored: LOW.")
elif score <=4:
    print("You scored: AVERAGE.")
else:
    print("You scored: PERFECT.")
    print("Good job!")

