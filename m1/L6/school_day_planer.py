"""
1) Add the activity details.
   a) Mention the activity name as "ATM Cash Dispenser".
   b) Introduce the program as a cash withdrawal and denomination tracker.

2) Display the welcome message.
   a) Print the ATM title.
   b) Explain that customers will be served one at a time.

3) Create starting variables.
   a) Store available note values in the `notes` list.
   b) Create `customers_served` to count total customers.
   c) Create `total_dispensed` to track total cash withdrawn.
   d) Create `log` to store each customer's note breakdown.

4) Use the outer while loop.
   a) Use `serving = True` to keep the ATM session running.
   b) Ask for the customer name and withdrawal amount.
   c) Use `continue` if the amount is invalid.

5) Break the amount into notes.
   a) Store the withdrawal amount in `remaining`.
   b) Use an inner while loop to check each note value.
   c) Use floor division `//` to calculate note count.
   d) Use subtraction to reduce the remaining amount.
   e) Store used notes in the `used` dictionary.

6) Update transaction records.
   a) Increase the number of customers served.
   b) Add the withdrawal amount to the total dispensed cash.
   c) Save the customer's note breakdown in `log`.
   d) Print a transaction complete message.

7) Ask for the next customer.
   a) Ask whether another customer should be served.
   b) Stop the outer loop if the answer is not "yes".

8) Create the daily denomination report.
   a) Use an outer for loop to go through each note value.
   b) Use an inner for loop to check every customer's note usage.
   c) Use `.get()` to safely read note counts from each record.
   d) Print only the notes that were dispensed.

9) Display the final summary.
   a) Print the total number of customers served.
   b) Print the total cash dispensed.
   c) Print the ATM session closing message.
"""


# ------------------Output-------------------------------
"""
=== Smart School Day Planner ===
Answer 3 quick questions and I will plan your day!

What day is it? (Monday to Sunday): Monday
What is the weather? (sunny / rainy / cloudy): rainy
Is your homework done? (yes / no): yes

=== Your Plan for Monday ===
-----------------------------------
Day type    : First day of the week. Pack your weekly planner.
Weather tip : Pack your umbrella - it may get wet outside.
Best plan   : Take it one step at a time - you have got this!

Plan complete! Have a wonderful day!
"""

""


# Topic 1 -- if-elif-else: classify the day


# Topic 2 -- AND operator: sunny AND homework done


# Topic 3 -- OR operator: rainy OR cloudy


# Topic 4 -- NOT operator: homework NOT done


# Topic 5 -- Combining AND + OR + NOT together

print("=== Smart School Day Planner ===")
print("Answer 3 quick questions and I will plan your day!")
day = input("What day is it? (Monday to Sunday): ")
weather = input("What is the weather? (sunny / rainy / cloudy): ")
homework = input("Is your homework done? (yes / no): ")

print("===", day, "===")
if day == "saturday" or day == "sunday":
    print("today is a weekend")
elif not day == "saturday" or day == "sunday":
    print("today is a weekday")

print("===", weather, "===")
if weather == "sunny" or weather == "cloudy":
    print("you can go outside")
elif not weather == "sunny" or weather == "cloudy":
    print("you cannot go outside without a umbrella")

print("===", homework, ("==="))
if homework == "yes":
    print("you can do what you want")
else:
    print("finish your homework")