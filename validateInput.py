while True:
    print("Enter your age")
    age = input()
    if age.isdecimal():
        break
    else:
        print("Enter a number for your age.")

while True:
    print("Select a new passowrd (letter and numbers only)")
    password = input()
    if password.isalnum():
        break
    else:
        print("Password can only have letters and numbers.")
