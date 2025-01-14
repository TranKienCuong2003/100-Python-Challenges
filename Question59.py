import re

email_address = input("Enter an email address: ")

pattern = r"(\w+)@(\w+)\.(com)"

match = re.match(pattern, email_address)

if match:
    print("Domain:", match.group(2))
else:
    print("Invalid email address")
