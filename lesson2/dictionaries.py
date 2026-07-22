# A Lecture on Python Dictionaries

# What is a dictionary in Python? 
# A dictionary is a collection of key-value pairs, 
# where each key is unique and maps to a specific value. 
# Dictionaries are mutable, meaning that their contents can be changed after they are created. 
# They are also unordered, meaning that the order of the items is not guaranteed.
# Dictionaries starts with a left curly brace { and ends with a right curly brace } 
# e.g. d = {key1: value1, key2: value2, key3: value3}

from itertools import count


ronaldo = {"name": "Cristiano Ronaldo", 
           "age": 41, 
           "position": "Forward", 
           "team": "Al Nassr", 
           "country": "Portugal"}

print(ronaldo["name"])  # Output: Cristiano Ronaldo
print(ronaldo["age"])  # Output: 41
print(ronaldo["position"])  # Output: Forward
print(ronaldo["team"])  # Output: Al Nassr
print(ronaldo["country"])  # Output: Portugal

print("Accessing dictionary values using the get() method:")

print(ronaldo.get("name"))  # Output: Cristiano Ronaldo
print(ronaldo.get("age"))  # Output: 41

# Updating dictionary values
ronaldo["age"] = 42
print("Ronaldo's age:", ronaldo["age"])  # Output: 42
ronaldo["position"] = "Midfielder"
print("Ronaldo's position:", ronaldo["position"])  # Output: Mid

ronaldo["country"] = "Spain"
print("Ronaldo's country:", ronaldo["country"])  # Output: Spain

# Next class: More of Dictionaries, if else statements, loops, and functions/methods in Python.

print(ronaldo)

# Dictionary Methods
print(ronaldo.keys())
print(list(ronaldo.keys())[0])

ronaldo_keys = ronaldo.keys()
ronaldo_keys_list = list(ronaldo_keys)
print(ronaldo_keys_list[2])  # Output: name

# Dictionary Values
ronaldo_values = ronaldo.values()
print(ronaldo_values)

# removing items
print(ronaldo.pop("position"))

print(ronaldo)

