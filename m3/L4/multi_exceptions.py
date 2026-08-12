try:
    num1 = input("Enter number: ")
    num2 = input("Enter number: ")
    num1 = int(num1)
    num2 = int(num2)
    div = num1/num2

except ValueError:
    print("enter a valid number")
    
except ZeroDivisionError:
    print("cannot divide by zero")

else:
    print("Result:", div, type(div))
finally:
    print("Thank you")