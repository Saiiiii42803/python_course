"""
Activity: Snack Vending Machine

Instructions:
1. Create a function to calculate the change.
2. Set the snack price and accepted coin values.
3. Keep accepting coins until enough money is inserted.
4. Reject any invalid coin using continue.
5. Stop accepting coins using break.
6. Calculate and display the change.
7. Use pass when there is no change to return.
8. Display the purchase summary.
"""



"""
OUTPUT:

===== SNACK VENDING MACHINE =====
Snack Price: 25
Accepted Coins: [1, 5, 10, 25]

Insert a coin: 4
Invalid coin! Please try again.

Insert a coin: 10
Total Inserted: 10
Insert a coin: 5
Total Inserted: 15
Insert a coin: 1
Total Inserted: 16
Insert a coin: 1
Total Inserted: 17
Insert a coin: 1
Total Inserted: 18
Insert a coin: 10
Total Inserted: 28

Dispensing your snack...
Change Returned: 3

===== PURCHASE SUMMARY =====
Snack Price    : 25
Coins Inserted : 6
Total Paid     : 28
Change Given   : 3
============================
Thank you for your purchase!
"""


# Create a function that returns the change



# Set the snack price and accepted coin values


# Keep accepting coins until enough money is inserted

    
    # Check whether the inserted coin is valid
   

    # Stop the loop once enough money has been inserted

# Calculate the change using the function


# Use pass when there is no change to return



# Display the purchase summary



snack_price = 25
coins_inserted = 0
total_inserted = 0
change_due = 0



'''
print("===== PURCHASE SUMMARY =====")
print("Snack Price    :", snack_price)
print("Coins Inserted :", coins_inserted)
print("Total Paid     :", total_inserted)
print("Change Given   :", change_due)
print("============================")
print("Thank you for your purchase!")
'''

while True:
    insert = int(input("insert a coin: "))
    if insert not in [1, 5, 10, 25]:
        print("please try again")
    else:
        coins_inserted += 1
        total_inserted += insert
        print("Total inserted:", total_inserted)
        if total_inserted >= 25:
            change_due = total_inserted - 25
            print()
            print("===== PURCHASE SUMMARY =====")
            print("Snack Price    :", snack_price)
            print("Coins Inserted :", coins_inserted)
            print("Total Paid     :", total_inserted)
            print("Change Given   :", change_due)
            print("============================")
            print("Thank you for your purchase!")
            break