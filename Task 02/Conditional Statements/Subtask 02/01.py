#A simple ATM withdrawal
correct_pin = 1234
account_balance = 500.00

entered_pin = int(input("Please enter your 4-digit PIN: "))

if entered_pin == correct_pin:
    print("PIN accepted.")
    
    withdrawal_amount = float(input("Enter amount to withdraw: $"))
    
    if withdrawal_amount > 0:
        
        if withdrawal_amount <= account_balance:
            
            if withdrawal_amount % 20 == 0:
                
                account_balance -= withdrawal_amount
                print(f"Success! Dispensing ${withdrawal_amount}.")
                print(f"Your new balance is ${account_balance}.")
                
            else:
                print("Error: This ATM only dispenses $20 bills.")
        else:
            print("Error: Insufficient funds in your account.")
    else:
        print("Error: Please enter a positive number.")
else:
    print("Error: Incorrect PIN. Transaction cancelled.")