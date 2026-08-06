
"""
Welcome to the Lemonade Stand!

Enter price per cup: 4
Enter number of cups sold: 10
Total Cost: 40.0

===== RECEIPT =====
Price Per Cup : 4.0
Cups Sold     : 10
Total Cost    : 40.0
Thank you for visiting!
===================
"""

name = input("enter your name: ")

def greet():
    print("Hello welcome to the lemonade stand:", name)
print()
greet()

price_cup = float(input("how much does a cup cost: "))
number_cups = int(input("how many cups did you buy: "))

def total_cost():
    print("total cost:", price_cup * number_cups)

total_cost()

print("===== RECEIPT =====")
print("Price Per Cup :", price_cup)
print("Cups Sold     :", number_cups)
total_cost()
print("Thank you for visiting!")
print("===================")