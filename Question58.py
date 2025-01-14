import re

email_address = input("Enter an email address: ")
pattern = r"(\w+)@((\w+\.)+(com))"
match = re.match(pattern, email_address)

if match:
    print("Username:", match.group(1))
else:
    print("Invalid email address")
