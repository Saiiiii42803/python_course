rows = int(input("enter number of rows: "))
num = int(1)
for row in range(rows):
    for col in range(row + 1):
        print(num, end=" ")
        num += 1
    print()
