'''
Dictionary - made up of Key/Value pairs
A Key's value can be: int, str, float, boolean, LIST, DICTIONARY
'''

students = {}
num_students = int(input("Enter the total number of students: "))

# Student's name (first name)
# Student's Home School
# Student's Age
# Student's Town


'''
What you DON'T want to do:

students = {'name': 'Hunter', 'school': 'Canton', 'Age': 17, 'Canton', 'name': ''} - key's have to be unique

Instead associate the one common element with an nested dictionary as that elements value
'''

for student in range(num_students):
    name = input("\nEnter the student's first name: ")
    school = input("Enter the student's school: ")
    age = int(input("Enter the student's age: "))
    town = input("Enter the student's town: ")

    # Store the data in a dictionary
    # The name variable as our key and create dictionary of the other variable keys/values as its value
    students[name] = {
        'School': school,
        'Age': age,
        'Town': town
    }

print(students)