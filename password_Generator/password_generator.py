import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

length = int(input("Enter the password length: "))

if length <= 0:
    print("Invalid input! Password length must be greater than 0.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

print("\nThank you for using the Password Generator!")