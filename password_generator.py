import random


def generate_pass():
    L1 = []
    for i in range(8):
        a = random.randint(48,122)
        L1.append(chr(a))
    for j in range(5):
        b = random.randint(32,39)
        L1.append(chr(b))
    for k in L1:
        print(k, end="")


def check_password():
    """Ask the user for a password and validate it, re-prompting until ALL criteria are met."""
    password = input("Enter your password: ")

    while True:
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_length = len(password) >= 13

        errors = []  

        if not has_length:
            errors.append("Password must be at least 13 characters long.")
        if not has_lower:
            errors.append("Password must contain at least one lowercase letter.")
        if not has_upper:
            errors.append("Password must contain at least one uppercase letter.")
        if not has_digit:
            errors.append("Password must contain at least one number.")

        if not errors:
            print("Your password is strong enough!")
            break  

        
        print("\nYour password does not meet the following criteria:")
        for e in errors:
            print(" -", e)

        password = input("\nRe-enter your password: ")


def main():
    print("Welcome to this password creator app:")
    print("\nMenu")
    print("""1. Me khud banaunga (I'll enter my own)
2. Tu password de (generate one for me)
3. Exit""")

    choice = int(input("Enter your choice from the options above: 1, 2, 3: "))

    if choice == 1:
        check_password()
    elif choice == 2:
        generate_pass()
    else:
        print("Thank you for visiting us!")


main()