import random
import string

def generate_password():
    # Define character sets for uppercase letters, digits, and symbols
    uppercase_letter = random.choice(string.ascii_uppercase)
    digits = random.choice(string.digits)
    symbols = random.choice('!$@')

    # Generate random characters for the remaining 5 positions
    remaining_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

    # Combine and shuffle the characters to create the password
    password_chars = uppercase_letter + remaining_chars + digits + symbols
    password = ''.join(password_chars)

    return password

# Generate and print 10 passwords
for _ in range(1000):
    password = generate_password()
    print(password)
