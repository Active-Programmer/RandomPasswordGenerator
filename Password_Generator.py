# Random password generator
# atleast 8 characters, 
# atleast 1 uppercase letters
# atleast 1 lowercase
# atleast 1 numeric number
# atleast 1 special characters
import random

upper_char_A = ["A","B","C","D","E","F","G","H"]
lower_char_a = ["a", "b", "c", "d", "e", "f", "g", "h"]
special_char = ["!", "@", "#", "$", "%", "&", "*", "^", "~"]

upper_char_I = ["I","J","K","L","M","N","O","P"]
lower_char_i = ["i", "j", "k", "l", "m", "n", "o", "p"]

random_upper_char = random.choice(upper_char_A)
random_lower_char = random.choice(lower_char_a)
random_special_char = random.choice(special_char)
random_numeric_char = random.randint(0,10)
random_upper_char1 = random.choice(upper_char_I)
random_lower_char1 = random.choice(lower_char_i)
# random_special_char1 = random.choice(special_char)
random_numeric_char1 = random.randint(0,10)

weak_password = random_upper_char + random_lower_char + random_special_char + str(random_numeric_char)

intermediate_password = weak_password + random_upper_char1 + random_lower_char1 + random_special_char + str(random_numeric_char1)


strong_password = str(random_numeric_char) + weak_password + intermediate_password + weak_password + random_upper_char + str(random_numeric_char)

print("1. Weak password")
print("2. Intermediate password")
print("3. Strong password")

while True:
    choice = int(input("Choose the password type(1-3) :"))
    if choice == 1:
        name_choice = input("Want to Add your name in the password?yes/no : ")
        if name_choice == "yes" or name_choice == "y":
            ask_first_name = input("Enter your first name :")
            ask_last_name = input("Enter the last name :")
            print("Password Generated :", ask_first_name + weak_password + ask_last_name)
        elif name_choice == "no" or name_choice == "n":
            print("password Generated : ", weak_password)
            
        else:
            print("Please give answer in 'yes' or 'no'!!")
    elif choice == 2:
        name_choice = input("Want to Add your name in the password?yes/no : ")
        if name_choice == "yes" or name_choice == "y":
            ask_first_name = input("Enter your first name :")
            ask_last_name = input("Enter the last name :")
            print("Password Generated : ", ask_first_name + intermediate_password + ask_last_name)
        elif name_choice == "no" or name_choice == "n":
            print("Password Generated : ",intermediate_password)
        else:
            print("Please give answer in 'yes' or 'no'!!")

    elif choice == 3:
        name_choice = input("Want to Add your name in the password?yes/no : ")
        if name_choice == "yes" or name_choice == "y":
            ask_first_name = input("Enter your first name :")
            ask_last_name = input("Enter the last name :")
            print("Password Generated : ", ask_first_name + strong_password + ask_last_name)
        
        elif name_choice == "no" or name_choice == "n":
            print("Password Generated : ", strong_password)
        else:
            print("Please give answer in 'yes' or 'no'!!")
    else:
        print("Please Enter the Correct Choice!! ")