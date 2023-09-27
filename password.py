import re

# Regular expression pattern for a 16-character alphanumeric password
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&+=!*_\-])[A-Za-z0-9@#$%^&+=!*_\-]{16}$'

# Test the regex pattern with sample passwords
passwords = [
    'Abcdefg123456789@',
    'P@ssw0rd12345678',
    'StrongP@ssw0rd!',
    'InvalidPassword1',
]

for password in passwords:
    if re.match(password_pattern, password):
        print(f"{password} is a valid 16-character alphanumeric password.")
    else:
        print(f"{password} is not a valid 16-character alphanumeric password.")
