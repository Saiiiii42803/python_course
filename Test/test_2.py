choice_result = int(input("Pick substraction-1, adition-2, division-3, multiplication-4: "))

if choice_result == 1:
    result = "SUB"
elif choice_result == 2:
    result = "ADD"
elif choice_result == 3:
    result = "DIV"
elif choice_result == 4:
    result = "MULT"

num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter a number: "))


if result == "SUB":
    try:
        print(num_1 - num_2)
    except ZeroDivisionError:
        print("Restart Code and try again cant use zero")
    except ValueError:
            print("Restart Code and try again has to be a number")
if result == "ADD":
    try:
        print(num_1 + num_2)
    except ZeroDivisionError:
        print("Restart Code and try again cant use zero")
    except ValueError:
            print("Restart Code and try again has to be a number")
if result == "DIV":
    try:
        print(num_1 / num_2)
    except ZeroDivisionError:
        print("Restart Code and try again cant use zero")
    except ValueError:
            print("Restart Code and try again has to be a number")
if result == "MULT":
    try:
        print(num_1 * num_2)
    except ZeroDivisionError:
        print("Restart Code and try again cant use zero")
    except ValueError:
            print("Restart Code and try again has to be a number")