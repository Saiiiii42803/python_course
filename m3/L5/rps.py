import random

choice_user = int(input("Enter a number 1-rock 2-papper 3-scissors: "))

choice_pc = random.randint(1, 3)

if choice_user == 1:
    choice = "rock"
elif choice_user == 2:
    choice = "papper"
elif choice_user == 3:
    choice = "scissors"



if choice_pc == 1:
    choicecc = "rock"
elif choice_pc == 2:
    choicecc = "papper"
elif choice_pc == 3:
    choicecc = "scissors"

if choice == choicecc:
    print("TIE")
elif choice == ("rock") and choicecc == ("papper"):
    print("You Lose")
elif choice == ("papper") and choicecc == ("scissor"):
    print("You Lose")
elif choice == ("scissors") and choicecc == ("rock"):
    print("You Lose")
else:
    print("You Win")

print(choice_pc)