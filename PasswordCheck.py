password = input("Enter a password:")

has_number = False
has_upper = False
# So bascially i interpreted these values as false so that when the for loop runs it chnages these values to True


for char in password:
    if char.isdigit():
        has_number = True
    if char.isupper():
        has_upper = True
# These set the values to True/False for the next lines of code that check the password       
if len(password) < 8:
    print("Password too short, must be over 8 characters.")
elif not has_number:
    print("Add numbers to the password.")
elif not has_upper:
    print("Add an uppercase letter.")
else:
    print("Password is strong enough")
    # Thanks