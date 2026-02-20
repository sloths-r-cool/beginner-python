operator = input("Select an operation: +, -, /, *,")
number1 = float(input("Enter 1st number:"))
number2 = float(input("Enter 2nd number:"))
# Converting these into floats allows python to properly carry mathematic equations, meaning numbers can be carried through equations rather than joining together.
if operator == "+":
    result = number1 + number2
    print(result)
elif operator == "-":
    result = number1 - number2
    print(result)
elif operator == "/":
    result = number1 / number2
    print(result)
# Important to use true divison so decimals can be shown instead of remainders for convenience.
elif operator == "*":
    result = number1 * number2
    print(result)
else:
    print("Invalid operator.")
    result = None
    print(result)
