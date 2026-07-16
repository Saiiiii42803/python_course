"""
Final output should look like something like below:
----------------------------------------------------

Enter today's temperature in Celsius: 20
It is warm today.
Wear a t-shirt
Is it raining today? (yes/no): yes
Bring an umbrella!
Enter the wind speed in km/h: 30
It is calm today.
No windbreaker needed over your t-shirt
Are there puddles on the ground? (yes/no): no
The ground is dry.
Wear sneakers

Weather check complete!
===== WEATHER OUTFIT PICKER =====
Temperature: 20
Outfit Chosen: t-shirt
Raining: yes
Windbreaker Needed: no
Shoes Chosen: sneakers
===================================
"""


# PART 1: Ask for today's temperature and take it as an integer input
temp = int(input("what is todays tempreture in celceus: "))
if temp > 20:
    outfit = "T-shirt"
else: 
    outfit = "Jacket"

raining = input("Is it raining yes/no: ")
if raining == "yes":
    print("umbrella")
else: 
    print("Sunglasses")

wind_speed = int(input("enter wind speed MPH: "))
if wind_speed > 30:
    wind_speed = "yes"
else:
    wind_speed = "no"

print("===== WEATHER OUTFIT PICKER =====")
print("Temperature: ", temp)
print("Outfit Chosen: ", outfit)
print("Raining: ", raining)
print("Windbreaker Needed: ", wind_speed)
print("===================================")
# PART 2: Decide between a jacket and a t-shirt


# PART 3: Ask whether it is raining


# PART 4: Add an umbrella reminder only if it is raining



# PART 5: Ask for the wind speed



# PART 6: Decide whether a windbreaker is needed



# PART 7: Ask whether there are puddles on the ground



# PART 8: Decide between boots and sneakers



# PART 9: This message always prints, no matter what was chosen above

