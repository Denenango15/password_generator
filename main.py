'''The program generates a user-defined number of passwords with a specified number of characters'''
import random
import string


def get_integer_input(prompt):
    """Prompt user to enter a positive integer"""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")


number = get_integer_input('How many passwords should I generate?\n')
length = get_integer_input('How many characters should be in the password?\n')


def generate_password(length):
    """Generate a random password"""
    letters = string.ascii_letters
    digits = string.digits
    symbols = '+-/*!&$#?=@<>'
    all_characters = letters + digits + symbols
    password = ''.join(random.choice(all_characters) for _ in range(length))

    # Ensure the password contains both letters and digits
    while not (any(char.isdigit() for char in password) and any(char.isalpha() for char in password)):
        password = ''.join(random.choice(all_characters) for _ in range(length))

    return password


# Generate and print the requested number of passwords
for i in range(number):
    print(generate_password(length))
