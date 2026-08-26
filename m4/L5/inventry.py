"""
Activity: School Store Inventory

Instructions:
1. Create a list of items and their stock quantities.
2. Create a dictionary by pairing each item with its stock.
3. Display the items that are currently in stock.
4. Ask the customer which item they want to buy.
5. Check whether the item is available.
6. Create a list of prices for the items.
7. Find and display the price of the selected item.
8. Reduce the stock by 1 after the purchase.
9. Display the updated inventory.
"""



"""
OUTPUT:

Inventory: {'pencil': 12, 'eraser': 0, 'notebook': 8, 'sharpener': 5, 'glue': 3}
Items in stock: ['pencil', 'notebook', 'sharpener', 'glue']
Which item do you want to buy? pencil
Price of pencil : 10
Purchase successful!

===== SCHOOL STORE SUMMARY =====
Item Bought      : pencil
Price Paid       : 10
Updated Inventory: {'pencil': 11, 'eraser': 0, 'notebook': 8, 'sharpener': 5, 'glue': 3}
================================
"""

# Create lists of items, stock quantities, and prices
items = ["pencil", "eraser", "notebook", "sharpener", "glue"]
stock = [12, 0, 8, 5, 3]
prices = [10, 5, 40, 15, 20]

inventory = dict(zip(items, stock))

print("inventory:", inventory)
instock = []
for k, v in inventory.items():
    if v > 0:
        instock.append(k)

print("In stock:", instock)


buy = input("which item do you want to buy: ")

print("cost -", buy, "10")
inventory[buy] -= 1
print("===== SCHOOL STORE SUMMARY =====")
print(inventory)
print("================================")
