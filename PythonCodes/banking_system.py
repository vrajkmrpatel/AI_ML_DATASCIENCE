# Try to solve this problem statement without using internet
 
# Write a program that:
# Accepts a list of transactions (strings):
# ["DEPOSIT 1000", "WITHDRAW 500", "WITHDRAW 700", "DEPOSIT 200"]
# Initial balance = 0
# Requirements:
# Process transactions
# Use conditionals to:
    # Add for DEPOSIT
    # Subtract for WITHDRAW
# Prevent overdraft (balance cannot go below 0)
# Handle invalid transaction formats
# Return final balance and number of failed transactions

lst: list[str] = ["DEPOSIT 1000", "WITHDRAW 500", "WITHDRAW 700", "DEPOSIT 200"]

balance = 0
failed_t = 0

for transaction in lst:
    try:
        action, amount_str = transaction.split()
        amount = int(amount_str)

        if action == "DEPOSIT":
            balance += amount
        elif action == "WITHDRAW":
            if balance < amount:
                print("Balance cannot go below 0")
                failed_t += 1
            else:
                balance -= amount
        else:
            print("Invalid transaction format")
            failed_t += 1
    except ValueError:
        print("Invalid transaction format")
        failed_t += 1
print("Final balance:", balance)
print("Number of failed transactions:", failed_t)    


# lst: list[str] = ["DEPOSIT 1000", "WITHDRAW 500","MSG 500", "WITHDRAW 700", "DEPOSIT 200"]

# def sort_by_amount(transaction):
#     try:
#         action, amount_str = transaction.split()
#         amount = int(amount_str)
#         return amount
#     except ValueError:
#         return float('inf')  # Place invalid transactions at the end
    
# sorted_lst = sorted(lst)
# print("Sorted transactions:", sorted_lst)
# sorted_lst_by_amount = sorted(lst, key=sort_by_amount)
# print("Sorted transactions by amount:", sorted_lst_by_amount)