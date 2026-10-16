
# Password Strength Checker

print("Welcome to the Password Strength Checker!")

password = input("Enter a password to check: ")

score = 0

if len(password) >= 8:
    score = score + 1

if any(char.isupper() for char in password):
    score = score + 1

if any(char.islower() for char in password):
    score = score + 1

if any(char.isdigit() for char in password):
    score = score + 1

if any(not char.isalnum() for char in password):
    score = score + 1

print("\nPassword Strength:")

if score <= 2:
    print("Weak password")
elif score <= 4:
    print("Medium password")
else:
    print("Strong password")

print("Thank you for using the program!")
