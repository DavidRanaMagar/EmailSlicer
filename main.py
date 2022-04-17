try:
    email = input("Enter a email address: ")
    print(f"Your user name is: {email[:email.index('@')]}")
    print(f"Your domain name is: {email[email.index('@') + 1:]}")
except ValueError:
    print(f"Your entry: \"{email}\" is not valid email address.")
