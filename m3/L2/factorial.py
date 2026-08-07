"""
Enter a num: 4
Factorial of 4: 24
5

(Reason 4! = 4 * 3 * 2 * 1 = 24)

"""

num = int(input("Enter a number: "))



def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

    

sum = fact(num)

print("factorial of", num,":", sum)