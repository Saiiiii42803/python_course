"""
Enter a num: 2
Cube of 2: 8

(Reason 2 x 2 x 2 = 8)
"""

num = int(input("Enter a number: "))

def cube(x):
    
    return x * x * x

sum = cube(num)

print("cube of", num,":", sum)