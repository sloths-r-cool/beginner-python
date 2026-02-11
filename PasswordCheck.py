password = input("Enter a password:")

has_number = False
has_upper = False

for char in password:
    if char.isdigit():
        has_number = True
    if char.isupper():
        has_upper = True
       
if len(password) < 8:
    print("Password too short, must be over 8 characters.")
elif not has_number:
    print("Add numbers to the password.")
elif not has_upper:
    print("Add an uppercase letter.")
else:
    print("Password is strong enough")