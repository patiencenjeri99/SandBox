# Set the minimum password length
MIN_LENGTH = 8

# Ask the user for a password with error checking
password = input("Enter a password: ")

while len(password) < MIN_LENGTH:
    print(f"Password must be at least {MIN_LENGTH} characters long.")
    password = input("Enter a password: ")

# Print asterisks equal to the password length
print("*" * len(password))
