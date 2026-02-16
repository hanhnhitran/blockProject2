# Password Strength Checker
password = input("Enter your password: ")

score = 0

#check length
if len(password) >= 8:
    score += 1

#check for uppercase
if any(c.isupper() for c in password):
    score += 1

#check for lowercase
if any(c.islower() for c in password):
    score += 1

#check for number
if any(c.isdigit() for c in password):
    score += 1

#check for symbol
symbols = "!@#$%^&*"
if any(c in symbols for c in password):
    score += 1

#show result
print("\nPassword Strength Result:")

if score <= 2:
    print("Weak password")
elif score == 3 or score == 4:
    print("Medium password")
else:
    print("Strong password")

print("Score:", score, "/ 5")
