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