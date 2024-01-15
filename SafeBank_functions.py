'''Banking app with a solid UI (user interface)
- Checking Balances
- Transferring Funds
- Depositing Money
- Withdrawing Money
- Checking Account limits
- Confirmation Prompts
'''
import random as rd

# defining functions for the users banking options, with built in account limit checking


# check balance function to check users balance (will return a randomly generated balance)

def check_bal():
    balance = rd.randint(100, 9999)
    return balance


# transfer function allowing user to transfer funds to another email account
# function will check user has enough funds (using a randomly generated balance)
# confirmation prompts to check amount to transfer and the users email address

def transfer():
    balance = rd.randint(100, 9999)
    
    while True:
        transfer_amount = float(input("\nPlease enter the amount you wish to transfer: £"))
        confirm_amount = float(input("Please confirm the amount you wish to transfer: £"))

        if balance >= transfer_amount and transfer_amount == confirm_amount:
            new_balance = balance - transfer_amount
            
            while True:
                transferee = input("\nPlease enter the email address of the account you wish to send funds to: ")
                confirm_transferee = input("Please confirm the email address of the account you wish to send funds to: ")

                if '@' in transferee and '.' in transferee and transferee == confirm_transferee:
                    confirm = input(f'''
Account email: {transferee}
Transfer amount: £{transfer_amount:.2f}

Do you wish to proceed with the transfer? (Yes/No)''').lower()
                    if confirm == 'yes':
                        print("\nTransfer successful.")
                        print(f"Your new balance is £{new_balance:.2f}")
                        break

                    elif confirm == 'no':
                        print("\nTransfer cancelled.")
                        break

                elif '@' in transferee and '.' in transferee and transferee != confirm_transferee:
                    print("\nAccount emails do not match, please try again.")
                    continue

                else:
                    print("\nInvalid Email, please try again.")
                    continue
            break

        elif transfer_amount > balance and transfer_amount == confirm_amount:
            print("\nYou have invalid funds to make this transfer.")
            break

        elif transfer_amount != confirm_amount:
            print("\nValues do not match, please try again.")
            continue

        else:
            print("\nPlease try again.")
            continue


# deposit function allowing user to deposit money into their account
# provides new balance following deposit
        
def make_deposit():
     balance = rd.randint(100, 9999)

     while True:
        try:
            deposit_amount = float(input("\nPlease enter the amount you wish to deposit: £"))
            confirm_amount = float(input("Please confirm the amount you wish to deposit: £"))

            if deposit_amount == confirm_amount:
                new_balance = balance + deposit_amount
                return new_balance

            elif deposit_amount != confirm_amount:
                print("Values do not match, please try again.\n")
                continue

        except ValueError: 
                print("Invalid input. Please try again.\n")
                continue


# withdrawal function allowing user to withdraw money from their account
# function will check user has enough funds (using a randomly generated balance)
# provides new balance following withdrawal
        
def make_withdrawal():
    balance = rd.randint(100, 9999)
    
    while True:
        withdrawal_amount = float(input("\nPlease enter the amount you wish to withdraw: £"))
        confirm_amount = float(input("Please confirm the amount you wish to withdraw: £"))

        if balance >= withdrawal_amount and withdrawal_amount == confirm_amount:
            new_balance = balance - withdrawal_amount
            print("\nWithdrawal successful.")
            print(f"Your new balance is £{new_balance:.2f}")
            break

        elif withdrawal_amount > balance and withdrawal_amount == confirm_amount:
            print("You have invalid funds to make this withdrawal.")
            break

        elif withdrawal_amount != confirm_amount:
            print("Values do not match, please try again.\n")
            continue

        else:
            print("Please try again.\n")
            continue