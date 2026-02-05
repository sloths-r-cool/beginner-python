score = 0

name = input("What is your name? ")
age = int(input("What is your age? "))

print(name + ", what is the first letter of the alphabet?")
answer = input()

if answer.lower() == "a":
    score = score + 1
    print("Correct. Your score is " + str(score))
else:
    print("Incorrect. Your score is " + str(score))
    
print("Next question")
print("What is 2*5?")
answer = input()
if answer == "10":
    score = score + 1
    print("Correct. Your score is " + str(score))
else:
    print("Incorrect. Your score is " + str(score))
print("Final question…")
print("Name a greeting.")
answer = input()
if answer.lower() == "hi":
    score = score + 1
    print("Correct! Your final score was " + str(score))
elif answer.lower() == "hello":
    print("Correct! Your final score is " + str(score))
else:
    print("I only would have accepted 'hi' or 'hello' because I lack immense brain capacity and IQ.")
    print("Your final score was…")
    print(str(score))
if score <= 1:
    print("Low…")
elif score == 2:
    print("Average.")
else:
    print("So smart…") 

    
    
     
