username = input("Enter your username: ")
password = input("Enter your password: ")

masked = '*' * len(password)

print(f"{username}, your password {masked} is {len(password)} characters long.")
