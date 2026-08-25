"""
Activity: Fruit Basket Organizer

Instructions:
1. Create two sets containing fruits in two baskets.
2. Add a new fruit to the first basket.
3. Find the fruits that are common to both baskets.
4. Create an array to store the number of fruits in each basket.
5. Add the number of fruits for a new basket.
6. Count how many baskets contain 5 fruits.
7. Reverse the array.
8. Display the final results.
"""

"""
OUTPUT:

===== FRUIT BASKET SUMMARY =====
Basket 1       : {'banana', 'grape', 'apple', 'mango', 'orange'}
Basket 2       : {'banana', 'mango', 'kiwi'}
Common Fruits  : {'banana', 'mango'}
Fruit Counts   : array('i', [5, 3])
===============================
"""
import array as arr

basket1 = {'banana', 'grape', 'apple', 'mango', 'orange'}
basket2 = {'banana', 'mango', 'kiwi'}

a = arr.array("i", [len(basket1), len(basket2)])
print(a)
print("===== FRUIT BASKET SUMMARY =====")
print("Basket1 =", basket1)
print("Basket2 =", basket2)
basket3 = basket1.intersection(basket2)
print("common fruits:", basket3)
print("Fruit count:", a)
print("================================")

