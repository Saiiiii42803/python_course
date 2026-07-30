"""
Enter the number whose sum you want to find: 3
Sum = 6
"""
user = int(input("Enter the number whose sum you want to find: "))
user = user + 1
sum = 0

for loop in range(1, user):
    sum = sum + loop
print(sum)