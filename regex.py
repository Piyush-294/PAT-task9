import re

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Test the regex pattern
emails = [
    'piyush@gmail.com',
    'invalid.email',
]

for email in emails:
    if re.match(email_pattern, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
