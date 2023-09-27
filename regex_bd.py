import re

# Regular expression pattern for matching Bangladeshi mobile phone numbers
bd_mobile_number_pattern = r'^880[0-9]{9}$'  # 880 is the country code for bangladesh

# Test the regex pattern with sample mobile numbers
mobile_numbers = [
    '880712345678',
    '880812345678',
    '8801912345678'
]

for number in mobile_numbers:
    if re.match(bd_mobile_number_pattern, number):
        print(f"{number} is a valid Bangladeshi mobile phone number.")
    else:
        print(f"{number} is not a valid Bangladeshi mobile phone number.")
