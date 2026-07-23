# Create an website age script to check ages. That takes age as input and checks if the user is eligible to use the website. 
# If the user is 18 years or older, they can access the website. 
# If they are younger than 18, they will be denied access. 
# The script should also handle invalid inputs (e.g., non-numeric values) gracefully.

# if else, elif, else statement

print("welcome to this adult website!! for you to access this website," \
" you be up to 18 years and above")

age_of_visitor = input("enter your age:  ")
age_of_visitor = int(age_of_visitor)    


if age_of_visitor >= 18:
    print("you have access to use this website")
    
elif age_of_visitor > 18:
    print("you have access to use this website")

elif age_of_visitor < 18:
    print("you do not have access to use this website")


else:
    print("you do not have access to use this website")

