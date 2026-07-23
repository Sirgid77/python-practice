# Converting to different datatypes
name = 18
name_string = str(name)
print("Converted", name_string)

# Convert from string to integer
name_integer = int(name_string)
print("Converted to integer:", name_integer)

# convert from integer to float

name_float = float(name_integer)
print("Converted to float: ", name_float)



# if else, elif, else statement

print("Welcome to my sportybet webstite!!! Pls you must be upto 18 years to use this website.")
visitor_age = input("Enter your age: ")
visitor_age = int(visitor_age)

# if statement: can only have one else block
# 18 - 20, should use teeengers website, while people from 20 and above will enter adult

if visitor_age >= 50:
    print("You are too old to be playing bet")
    print("You are not eligible to use the website.")
    print("Thank you for visiting my website, have a nice day!!!")

elif visitor_age > 20:
    print("You can enter the adult website")
elif visitor_age > 18:
    print("You can enter the teen website")
else:
    print("You are not eligible to use the website.")

print("You are eligible to use the website.")    

print("Thank you for visiting my website, have a nice day!!!")


