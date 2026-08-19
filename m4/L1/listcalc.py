lst = [100, 4, 2, 5, 3]
#lst.sort()

sum = 0
change = 0
for num in lst:
    sum = lst[change] + sum
    change += 1
    print(sum)
    