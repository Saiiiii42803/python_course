"""
1) Add the activity details.
   a) Mention the activity name as "Custom Ride Builder".
   b) Mention the file name as `ride_builder.py`.
   c) Mention the lesson as "Nested Conditional Statements".

2) Display the welcome message.
   a) Print a title banner for the ride builder.
   b) Add blank lines to keep the output neat.

3) Show the first vehicle choices.
   a) Display Bike as option 1.
   b) Display Car as option 2.
   c) Ask the user to enter 1 or 2.

4) Check the main choice.
   a) Use `if` when the user chooses Bike.
   b) Use `elif` when the user chooses Car.
   c) Use `else` for an invalid choice.

5) Use nested conditions for Bike.
   a) Show bike type options only if the user picked Bike.
   b) Ask the user to choose Scooty or Mountain Bike.
   c) Use an inner `if-else` to display the selected bike details.

6) Use nested conditions for Car.
   a) Show car type options only if the user picked Car.
   b) Ask the user to choose Sedan or SUV.
   c) Use an inner `if-else` to display the selected car details.

7) Display ride details.
   a) Print the selected ride name.
   b) Print speed or seat information.
   c) Print what the ride is best used for.

8) Handle invalid input.
   a) Show an error message if the first choice is not 1 or 2.
   b) Ask the user to enter the correct option next time.

9) End the program.
   a) Print a closing banner.
   b) Display a message saying the custom ride is ready.
"""

# OUTPUT

"""
====================================
      Welcome to Ride Builder!      
====================================

Step 1: Pick your vehicle
  1 - Bike
  2 - Car

Enter 1 or 2: 2

Step 2: Pick your car type
  1 - Sedan
  2 - SUV

Enter 1 or 2: 1

You picked  : Sedan
Best for    : Family trips

====================================
   Your custom ride is ready!       
   Enjoy the journey!               
====================================

"""



print("====================================")
print("     Welcome to Ride Builder!")     
print("====================================")

print(" pick your vehicle")
print("1. - car")
print("2. - bike")
vehicle = int(input("enter 1 or 2: "))

if vehicle == 1:
    print(" pick your car")
    print("1. - sedan")
    print("2. - suv")
    car = int(input("enter 1 or 2: "))
    if car == 1:
        print("Sedan")
    else:
        print("Suv")
else:
    print(" pick your bike")
    print("1. - sport")
    print("2. - mountain")
    bike = int(input("enter 1 or 2: "))
    if bike == 1:
        print("sport")
    else:
        print("mountain")

