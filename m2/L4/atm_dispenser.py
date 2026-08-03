"""
Activity: ATM Cash Dispenser

Instructions:
1. Ask the user to enter their name.
2. Ask for the withdrawal amount.
3. Use a nested while loop to calculate the number of notes.
4. Display the notes given to the customer.
5. Ask if another customer wants to use the ATM.
6. After all customers are served, display:
   - Total customers served
   - Total money dispensed
   - Total notes of each denomination
7. Use a nested for loop to print one '*' symbol for each note dispensed.
"""

"""
Output:
=== ATM Cash Dispenser ===

Enter customer name: Ajay
Enter withdrawal amount: 110

Dispensing 110 units:

1 x 100 unit note(s)
1 x 10 unit note(s)

Serve another customer? (yes/no): yes
Enter customer name: Guna
Enter withdrawal amount: 250

Dispensing 250 units:

2 x 100 unit note(s)
1 x 50 unit note(s)

Serve another customer? (yes/no): no

=== Daily Report ===
Customers Served : 2
Total Amount Dispensed : 360
ATM Closed
"""

index = 0
count = 0
name = input("Enter customer name: ")
withdrawal = int(input("Enter withdrawal amount: "))
notes = [100, 50, 20, 10, 1]
customer_served = 0
total_amount = 0
remaining = 0

print("======= ATM open =======")
print(name)
while True:
    index = 0
    withdrawal = int(input("Enter withdrawal amount: "))
    if withdrawal <= 0 :
        print("enter valid amount: ")
        print(withdrawal)
        continue
    remaining = withdrawal
    while True:
        count = remaining // notes [index]
        if count > 0:
            print(count, "x", notes [index], "unit note(s)")
            remaining = remaining % notes [index]
        index = index + 1
        if remaining <= 0:
            break
    customer_served = customer_served + 1
    total_amount = total_amount + withdrawal
    choice = input("Serve another customer? Yes/No: ")
    if choice == "yes":
        continue
    else:
        break
print("=== Daily report ===")
print(customer_served)
print(total_amount)