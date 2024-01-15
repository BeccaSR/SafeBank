'''Banking app with a solid UI (user interface)
- Checking Balances
- Transferring Funds
- Depositing Money
- Withdrawing Money
- Checking Account limits
- Confirmation Prompts
'''
from SafeBank_functions import *

# welcome message and user log in, with input validation for email and PIN
print("Welcome to SafeBank Banking App!\n")

while True:
    user_email = input("Please enter your email address: ")

    if '@' in user_email and '.' in user_email:
        print("Valid Email.\n")
    else:
        print("Invalid Email, please try again.\n")
        continue

    user_pin = input("Please enter your PIN: ")

    if len(user_pin) == 4 and user_pin.isdigit():
        print("User PIN accepted.\n")
        break

    else:
        print("Invalid PIN, please try again. \n")

# confirmation of successful log in, providing user with options
print("Log in successful. Please make a selection from the below menu.")

while True:
    try:
        print("""
        1. Check your current balance
        2. Transfer funds
        3. Make a deposit
        4. Make a withdrawal
        5. Log out
        """)

        choice = int(input("Please enter the option number you wish to proceed with: "))

        # if-elif statements for each option in menu, user asked to confirm PIN before proceeding with selected option
        if choice == 1:

            while True:
                confirm_pin = input("\nPlease enter your PIN to confirm action 'Check your current balance': ")

                if user_pin == confirm_pin:
                    current_balance = check_bal()
                    print(f"\nYour current balance is £{current_balance:.2f}")
                    break
                else:
                    print("Incorrect PIN")

            continue

        elif choice == 2:

            while True:
                confirm_pin = input("\nPlease enter your PIN to confirm action 'Transfer funds': ")

                if user_pin == confirm_pin:
                    transfer()
                    break
                else:
                    print("Incorrect PIN")

            continue

        elif choice == 3:

            while True:
                confirm_pin = input("\nPlease enter your PIN to confirm action 'Make a deposit': ")

                if user_pin == confirm_pin:
                    new_balance = make_deposit()
                    print("\nDeposit successful.")
                    print(f"Your new balance is £{new_balance:.2f}")
                    break
                else:
                    print("Incorrect PIN")

            continue

        elif choice == 4:

            while True:
                confirm_pin = input("\nPlease enter your PIN to confirm action 'Make a withdrawal': ")

                if user_pin == confirm_pin:
                    make_withdrawal()
                    break
                else:
                    print("Incorrect PIN")

            continue

        elif choice == 5:
            print("\nYou have successfully logged out.")
            break

        else:
            print("\nInvalid choice, please enter your selection again.")
            continue

    except ValueError:
        print("\nIncorrect selection, please enter a number selection.")
        continue
