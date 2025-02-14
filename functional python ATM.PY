import time  # Importing time module for sleep function

print("Please Insert Your CARD")  # Simulating card insertion message

time.sleep(3)  # Delay of 3 seconds to mimic real ATM behavior

password = 1234  # Predefined PIN for authentication
pin = int(input("Enter Your CARD PIN"))  # User enters PIN

Balance = 50000  # Initial balance in the account

# Checking if the entered PIN is correct
if pin == password:  
    while True:  # Infinite loop to keep the ATM menu running
        print("""
            1 == Balance
            2 == Withdraw balance
            3 == Deposit balance
            4 == Exit
            """
        )  # Displaying menu options
        
        try:
            option = int(input("Please Enter Your Choice"))  # User selects an option
        except:
            print("Please Enter Valid Option")  # Error handling for invalid input

        # Option 1: Checking balance
        if option == 1:
            print(f"Your Current Balance is {Balance}")
            print("===============================")

        # Option 2: Withdrawing money
        if option == 2:
            Withdraw_amount = int(input("Please Enter Withdraw Amount"))
            print("===============================")
            Balance = Balance - Withdraw_amount  # Deducting the amount
            print(f"{Withdraw_amount} is Debited From Your Account")
            print("===============================")
            print(f"Your Updated Balance is {Balance}")
            print("===============================")

        # Option 3: Depositing money
        if option == 3:
            Deposit_amount = int(input("Please Enter Deposit Amount"))
            print("===============================")
            Balance = Balance + Deposit_amount  # Adding the deposited amount
            print(f"{Deposit_amount} is Credited To Your Account")
            print("===============================")
            print(f"Your Updated Balance is {Balance}")
            print("===============================")

        # Option 4: Exiting the ATM
        if option == 4:
            break  # Exiting the loop and ending the program

else:
    print("Wrong PIN Please Try Again")  # Message for incorrect PIN