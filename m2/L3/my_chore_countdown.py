"""

INSTRUCTIONS

Chore Countdown (While Loop)

1. Create a list of 4 chores.
2. Store the total number of chores in a variable called `remaining`.
3. Create another variable called `index` and set it to 0.
4. Display the total number of chores to the user.
5. Use a while loop that runs while there are chores remaining.
6. Inside the loop:
   - Ask the user if they have completed the current chore.
   - If the answer is "yes":
       * Decrease the number of remaining chores by 1.
       * Move to the next chore by increasing the index.
       * Display a congratulatory message.
   - Otherwise, remind the user to finish the chore first.
7. After each attempt, display how many chores are remaining.
8. When all chores are completed, display a final completion message.
"""


"""
OUTPUT:

You have 4 chores to finish today!

Did you finish Make your bed? (yes/no): no
Finish it first!
Chores remaining: 4

Did you finish Make your bed? (yes/no): yes
Great job!
Chores remaining: 3

Did you finish Feed the pet? (yes/no): yes
Great job!
Chores remaining: 2

Did you finish Take out the trash? (yes/no): yes
Great job!
Chores remaining: 1

Did you finish Wash the dishes? (yes/no): no
Finish it first!
Chores remaining: 1

Did you finish Wash the dishes? (yes/no): no
Finish it first!
Chores remaining: 1

Did you finish Wash the dishes? (yes/no): yes
Great job!
Chores remaining: 0

All chores are complete!
"""



# List of chores to complete



# Define remaining and index variables. remaining for storing remaining chores and index for current chore


# print the remaining to chores to finish
# print("You have", remaining, "chores to finish today!\n")



# Repeat until there are no chores left


    # Ask if the current chore is finished
    

    # Move to the next chore only if the current one is completed
    

    # Display the countdown after each check
    



# Runs after all chores are completed





chores_left = 4

chores  = ["make your bed", "eat your breakfast", "Get ready", "go to school"]

while chores_left >= 0:
    answer = input("Did you finish Make your bed? yes/no: ")
    if answer == "yes":
        print("good job")
        chores_left = chores_left - 1
        print("Chores remaining:", chores_left)
        print()
        break
    else:
        print()
        print("Finish it first!")
        print("Chores remaining:", chores_left)




while chores_left >= 0:
    answer = input("Did you eat your breakfast? yes/no: ")
    if answer == "yes":
        print("good job")
        chores_left = chores_left - 1
        print("Chores remaining:", chores_left)
        print()
        break
    else:
        print()
        print("Finish it first!")
        print("Chores remaining:", chores_left)




while chores_left >= 0:
    answer = input("Did you get ready for school? yes/no: ")
    if answer == "yes":
        print("good job")
        chores_left = chores_left - 1
        print("Chores remaining:", chores_left)
        print()
        break
    else:
        print()
        print("Finish it first!")
        print("Chores remaining:", chores_left)




while chores_left >= 0:
    answer = input("Did you got to school yes/no: ")
    if answer == "yes":
        print("good job")
        chores_left = chores_left - 1
        print("Chores remaining:", chores_left)
        print()
        break
    else:
        print()
        print("Finish it first!")
        print("Chores remaining:", chores_left)



if chores_left == 0:
    print("You have finished everything.")