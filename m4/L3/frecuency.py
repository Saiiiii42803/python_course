"""
Activity: Count Students with a Particular Mark

Instructions:
1. Create a dictionary containing student names and their marks.
2. Ask the user for a mark to search for.
3. Use a for loop to check each student's mark.
4. Count how many students have the selected mark.
5. Display the result.
"""


"""
OUTPUT:

Student Marks: {'Aman': 80, 'Riya': 90, 'Rahul': 80, 'Sneha': 75, 'Arjun': 90}
Enter a mark to search for: 80
Number of students with 80 marks: 2
"""

# Store student names and their marks in a dictionary
marks = {
    "Aman": 80,
    "Riya": 90,
    "Rahul": 80,
    "Sneha": 75,
    "Arjun": 90
}

print("Student Marks:", marks)

get = int(input("Pick marks to get from list: "))
count = 0
for k, v in marks.items():
    if v == get:
        count += 1
print(f"frecuency: {count}")