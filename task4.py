# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people = ["John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole"]

number = int(input("Enter a number less than 10: "))

if number < 10:
    print(people[number])

else:
    print("Invalid input")