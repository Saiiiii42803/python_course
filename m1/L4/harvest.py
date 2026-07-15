"""
1) Add the activity details.
   a) Mention the activity name as "Farm Harvest Calculator".
   b) Introduce the program as a harvest and earnings calculator.

2) Store harvest values.
   a) Use the assignment operator `=` to store harvest from five fields.
   b) Store each field's harvest in separate variables.

3) Use arithmetic operators.
   a) Use `+` to calculate the total harvest.
   b) Use `/` to calculate the average harvest per field.
   c) Use `*` to calculate total earnings.

4) Display total, average, and earnings.
   a) Print the total harvest in kilograms.
   b) Print the average harvest per field.
   c) Print the total earnings in rupees.

5) Use floor division and modulus.
   a) Use `//` to calculate the number of full 25 kg bags.
   b) Use `%` to calculate the leftover grain.
   c) Print the full bags and leftover amount.

6) Use comparison operators.
   a) Compare this year's harvest with last year's harvest.
   b) Use `>` to check if this year is better.
   c) Use `==` to check if both years are the same.
   d) Use `>=` to check if this year is at least as good.

7) Use assignment operators.
   a) Use `+=` to add bonus crop to the total.
   b) Use `-=` to subtract grain saved as seeds.
   c) Print the updated harvest after each change.

8) Calculate the final bag count.
   a) Use floor division again after adjustments.
   b) Print the final number of bags packed.
"""

f1 = 120
f2 = 85
f3 = 150
f4 = 95
f5 = 110
total = f1 + f2 + f3 + f4 + f5
average = total / 5
print("-----------average:", average, "-----------")
print("-----------total:", total, "---------------")
price_kg = 15
print("---------total earings:", price_kg * total, "--------")
print("---------bags needed:", total // 25, "------------")
print("----------Kg remaining:", total % 25, "----------")

total += 30

harvest_last = 500
print("--- Better than last year?:", harvest_last > total, "---")

print("---------total earings:", price_kg * harvest_last, "--------")

print("------harvest after bonus:", total, "------")