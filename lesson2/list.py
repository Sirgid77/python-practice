# List Data Type
# What is the meaning of list in python? List is a collection of items in a particular order. 
# It is one of the most commonly used data types in Python. 
# Lists are mutable, meaning that their elements can be changed after the list has been created. 
# They can contain elements of different data types, including other lists.


fruits = ["apple", "banana", "cherry", "date", "mango"]
# List index starts from 0, so the first element is at index 0, the second at index 1, and so on.
print(fruits[0])  
print(fruits[1]) 

# List Slicing

print("The last fruit in the list is: ", fruits[-1])  # Output: mango (negative indexing starts from the end of the list)
print("The second last fruit in the list is: ", fruits[-2])  # Output: date

print("The first three fruits in the list are: ", fruits[0:5])  # Output: ['apple', 'banana', 'cherry'] (slicing the list)

print("The fruits from index 2 to the end are: ", fruits[2:])  # Output: ['cherry', 'date', 'mango'] (slicing from index 2 to the end)
print("The fruits from the start to index 3 are: ", fruits[:3])  # Output: ['apple', 'banana', 'cherry'] (slicing from the start to index 3)
print("The fruits from index 1 to index 4 are: ", fruits[1:4])  # Output: ['banana', 'cherry', 'date'] (slicing from index 1 to index 4)

# Python list are dynamic, meaning that they can grow and shrink in size as needed.
# Python lists can contain elements of different data types, including other lists.
cars = ["Toyota", 40.7, "Honda", "Ford", "Chevrolet", "BMW", 200, True, False, ["Mercedes", "Audi", "Volkswagen"]]

print("The first float in the list is: ", cars[1])

print("The full car list is: ", cars)

print("___________________________________" \
"___________________________")
# Modifiying Items in a list

fruits[0] = "Coconut"

print("The modified list is: ", fruits)  # Output: Coconut

fruits[4] = "Pineapple"

print("The modified list is: ", fruits)  # Output: Coconut

# Built-in List Functions
print("The length of the list is: ", len(fruits))  # Output: 5 (length of the list)

# Max and min in list

correct_score = [90, 85, 92, 88, 95]
print("The maximum score is: ", max(correct_score))  # Output: 95
print("The minimum score is: ", min(correct_score))  # Output: 85
print("The sum of the scores is: ", sum(correct_score))  # Output: 450

# Most popular list methods in Python are append(), insert(), remove(), pop(), clear(), index(), 
# count(), sort(), reverse() and copy().

more_scores = [75, 80, 85, 90, 95]

correct_score.append(more_scores)  # Appending a list to another list
print("The updated list is: ", correct_score)  # Output: [90, 85, 92, 88, 95, [75, 80, 85, 90, 95]]
# Getting a sublist or nested list.

print("The nested list zero index is: ", correct_score[5][0])

# insert function

correct_score.insert(2, 2000)  # Inserting an item at a specific index  
print("The updated list after inserting an item is: ", correct_score)  # Output: [90, 85, 2000, 92, 88, 95, [75, 80, 85, 90, 95]]

correct_score.remove(2000)  # Removing an item from the list
print("The updated list after removing an item is: ", correct_score)  # Output:

