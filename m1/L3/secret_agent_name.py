"""
1) Ask for agent details.
   a) Ask the user to enter their real name.
   b) Ask the user to enter their favourite gadget.
   c) Store both inputs as text values.

2) Store agent information.
   a) Create variables for agent number, speed rating, mission count, height, and active status.
   b) Use different data types such as integer, float, string, and Boolean.

3) Display each value and its data type.
   a) Print the agent name and gadget.
   b) Print number, rating, mission count, height, and active status.
   c) Use `type()` to show the data type of each value.

4) Convert values into text.
   a) Use `str()` to convert numbers into strings.
   b) Convert the Boolean value into text.
   c) Print the converted values and their new data types.

5) Create a secret code name.
   a) Use slicing to get the first three letters of the name.
   b) Use negative indexing to get the last letter.
   c) Join both parts to create the code name.

6) Reverse the gadget name.
   a) Use slicing with `[::-1]` to reverse the gadget text.
   b) Print the reversed gadget name.

7) Build the badge message.
   a) Create separate lines for the agent badge.
   b) Use string concatenation to join text and variables.
   c) Use `.upper()` to make important badge text uppercase.

8) Print the secret agent badge.
   a) Print a badge heading.
   b) Print all badge lines one by one.
   c) Print a closing line to complete the badge.
"""

name = input("what is your name: ")
gadget = input("what is your favortie gadget: ")
agent_number = int(input("what is your agent number: "))
speed_rating = float(input("whats your speed raiting from a scale of 1-10: "))
mission_count = int(input("how many missons have you completed: "))
agent_height = float(input("whats your height in inches: "))
is_active = input("is stil active true/false: ")

if is_active == "true":
    is_active = True       
elif is_active == "false":
    is_active = False
else:
    is_active = False

print("is_active: ", is_active, "type: ", type(is_active))




# ------------------ Display secret code -------------------

print("===== Secret Agent Badge =====")
print("AGENT:", name)
print("ID", agent_number, "| Missions:", mission_count)
print("Speed:", speed_rating, "| Active:", is_active)
print("Agent gadget:", gadget[::-1])
print("==============================")
# --------------------------------------------