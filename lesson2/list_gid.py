
# Assignment: Using the list below do the following:

long_list_of_cars = ["Toyota", "Honda", "Ford", "Chevrolet", "BMW", "Mercedes", "Audi", 
                     "Volkswagen", "Nissan", "Hyundai", "Kia", "Mazda", "Subaru", "Jeep", 
                     "Dodge", "Ram", "GMC", "Lexus", "Acura", "Infiniti"]

# 1. Print the first car in the list.
# 2. Print the last car in the list.
# 3. Print the first five cars in the list.
# 4. Print the last five cars in the list.

print(long_list_of_cars[0])  # Output: Toyota

print(long_list_of_cars[-1])  # Output: Infiniti

print(long_list_of_cars[0:5])  # Output: ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW']

print(long_list_of_cars[-5:])  # Output: ['Dodge', 'Ram', 'GMC', 'Lexus', 'Acura']



# Write 10 python list methods and explain what they do.

# 1: extend(): Appends all items from another iterable 
# (like a list or tuple) to the current list

nums = [1, 2, 3, 4, 5]
nums.extend([6, 7, 8])
print(nums)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# 2: pop(): Removes and returns the item at a specific index.
#  If no index is given, it removes the last item.

nums = [1, 2, 3, 4, 5]
nums.pop(3)  # Removes the item at index 3 (which is 4)
print(nums)  # Output: [1, 2, 3, 5]
nums.pop()  # Removes the last item (which is 5)
print(nums)  # Output: [1, 2, 3]

# 3: clear(): Removes all items from the list,
#  resetting it to an empty list.

Nigerian_cities = ["Umuahia", "Lagos", "Abuja", "Kano", 
                   "Port Harcourt","Ibadan"]
Nigerian_cities.clear()
print(Nigerian_cities)  # Output: []

# 4: count()Counts and returns how many times 
# an element appears in the list

nums = [1, 2, 3, 4, 5, 3]
nums.count(3) # Output: 2 (3 appears twice in the list)
print(nums)  # Output: [1, 2, 3, 4, 5, 3]
print(nums.count(3))  # Output: 2

# 5: sort(): Sorts the elements of the list in place 
# (modifies the original list directly).

nums = [10, 3, 5, 6, 9, 1,15, 2]
nums.sort()  # Sorts the list in ascending order
print(nums)  # Output: [1, 2, 3, 5, 6, 9, 10, 15]

# 6: reverse(): Reverses the elements of the list in place.
num = [1, 2, 3, 5, 6, 9, 10, 15]
num.reverse()  # Reverses the list
print(num)  # Output: [15, 10, 9, 6, 5, 3, 2, 1]


# 7: insert():Inserts a target element at
#  a specific index position.

nums = [2, 4, 5]
nums.insert(1, 3)  # Inserts 3 at index 1
print(nums)  # Output: [2, 3, 4, 5] 

# 8: remove()Deletes the first occurrence of 
# a specific value from the list

nums = [1, 2, 3, 4, 5, 3]
nums.remove(3)  # Removes the first occurrence of 3 
print(nums)  # Output: [1, 2, 4, 5, 3]

# 9: len(): Returns the total number of items in the list

nums = [1, 2, 3, 4, 5]
len(nums)  # Output: 5 (there are 5 items in the list)
print(len(nums))  # Output: 5

# 10: list()Converts an iterable object 
# (like a string, tuple, or set) into a list.

text = "Hello"
text_list = list(text)  # Converts the string into a list of characters
print(text_list)  # Output: ['H', 'e', 'l', 'l', 'o'] 

text = "Hello"
text_list = list(text)  # Converts the string into a list of characters
print(text_list)  # Output: ['H', 'e', 'l', 'l', 'o'] 

text = "Hello"
print(list(text))  # Output: ['H', 'e', 'l', 'l', 'o']

# 11: zip(): Aggregates elements from two or more lists into tuples.

names = ["Gideon", "Sistus"]
ages = [29, 27]
print(list(zip(names, ages)))  # Output: [('Gideon', 29), ('Sistus', 27)]








