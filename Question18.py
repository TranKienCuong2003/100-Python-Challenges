import re

def check_password_validity():
    passwords = input("Enter comma-separated passwords: ").split(",")
    valid_passwords = []

    for password in passwords:
        if (6 <= len(password) <= 12 and
            re.search(r"[a-z]", password) and
            re.search(r"[0-9]", password) and
            re.search(r"[A-Z]", password) and
            re.search(r"[$#@]", password)):
            valid_passwords.append(password)

    print(",".join(valid_passwords))

check_password_validity()
