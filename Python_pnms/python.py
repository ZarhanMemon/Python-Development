# This is my code in python 

print("I like burgers")
print("Its really salty")


#-----------------------------------------------------


# Variable - A reusable container to store a value ( int , floor , string , boolean)
#            The variable behaves as if it was the value it contains


full_name = "Zarhan Memon"  # string - sequence of characters
age = 19                    # int = integer ( whole number)
cgpa = 7.5                  # float - decimal number
is_student = False          # boolean - True or False

print(f"Name : {full_name}")
print(f"Age : {age}")
print(f"CGPA: {cgpa}")
print(f"Are you a student : {is_student}")  # f-string - formatted string for writing variables inside string


if is_student :
    print("I am a Student")
else:
    print("I am not a Student")


# ----------------------------------------------

# Arithmatic =  +  += addition
#               -  -= subtraction
#               *  *= multiplication
#               /  /= division ( return float)
#              // //= integer division (wireturn as integer)
#               %  %= remainder of division
a = 5

a += 1   # shorthand for a = a + 1
a -= 1   # shorthand for a = a - 1
a *= 2   # shorthand for a = a * 2
a /= 2   # shorthand for a = a / 2    = 5.0 (float)
a //= 2  # shorthand for a = a // 2   = 5   (int)
a %= 2   # shorthand for a = a % 2    = 1    

print(a)


# -------------------------------------------------


# Type Casting - The process of converting one data type to another data type
#                str()  , int()  , float() , bool()

name = "Zarhan Memon"
age = 19
cgpa = 7.5
is_student = True

print(type(is_student))      

cgpa = int(cgpa)
age = float(age)
is_student = int(is_student)
name = bool(name)
#name = int(name)   # Error: cannot convert string to int

age = str(age)
#age += 1       # Error: cannot concatenate str and int

age += "1"
print(cgpa , age , is_student , name )   


# ----------------------------------------------

# Input - Taking input from user

name = input("Enter your name: ")   # by default input is string

age =  int(input("Enter your age: ")) 
#age = int(age)   # type casting string to int

age += 1

print(type(name) ,  type(age))

print(f"Hello , {name} !")
print(f"You are {age} years old.")


# ----------------------------------------------

# if , elif , else - execute code based on condition
#                     they allow for decision making in code
#                     ( if , elif , else)

age = int(input("Enter your age: "))

has_ticket = True
price = 100.0

if age >= 65:
    print("You are a senior citizen.")
    print("You get a discount of 50%.")
    print(f"Your ticket price is: ${price * 0.5}")

elif age >= 18:
    print("You are an adult.")
elif age < 0:
    print("Invalid age entered.")
elif age == 0:                          # for checking  exact value
    print("You are a newborn.")
else:
    print("You are a minor.")
    print(f"Your ticket price is: ${price * 0.25}")


if has_ticket:  # has_ticket == True ->no need to write this
    print("You can enter the event.")
else:
    print("You cannot enter the event without a ticket.")


# ----------------------------------------------

# Logical Operators - used to combine conditional statements
#                     and - both conditions must be true
#                     or - either condition can be true
#                     not - invert a condition

temp = 25
is_raining = True

if temp <0 or temp > 35 or is_raining:
    print("The no outdoor activities.")
else:
    print("You can enjoy outdoor activities.")


if temp <= 0 or temp >= 35 and  is_raining:
    print("The weather is not nice for outdoor activities.")

if not is_raining:
    print("It is not raining today.")
else:
    print("It is raining today.")


# ----------------------------------------------


# While Loop - repeatedly execute a block of code as long as a condition is true

name = input("Enter your name: ")
age = int(input("Enter your age: "))

while name == "":
   name = input("Enter your name: ")

while age <= 0:
   print("Invalid age. Please enter a valid age.")
   age = int(input("Enter your age: "))

print(f"Hello, {name}!")
print(f"You are {age} years old.")


# ----------------------------------------------

# For Loop - used to iterate over a sequence ( list , string , range)

for i in range(1 , 10 + 1 , 3):   # start , end , step_skip
    print(f"Iteration {i}")   


name = "Zarhan Memon"

for letter in name:
    print(letter , end="-")  # endswith = "-" , after each letter of name



# -------------------------------------------------------

# MODULE - 

import time

for i in range(10 , -1 , -1): # 10-> 0 reverse order => step_skip = -1
    print(i)
    time.sleep(1)  # DELAY OF 1sec

print("Happy New Year !")


# ---------------------------------------------------------


# List []  = mutable (append/remove/pop/clear / list.[ ] = _), most flexible
# Tuple () = immutable , faster , NO indexing changes
# Set {}   = mutable (add/remove/clear) , unorderd , NO indexing/pop changes
#            No duplicated , best for membership testing



# LIST
fruits = ["apple" , "banana" , "coconut"]

fruits[0] = "mango"
fruits.append("grapes")
fruits.remove("coconut")
fruits.pop(2)              # delete elm by index given
fruits.clear()     # deletes all the elm in list


print(fruits[1])  # indexing 

for fruit in fruits:
    print(fruit ,  end=" ")


# ---------------------


#TUPLE
numbers = ( 1 ,2 , 3, 4)

# numbers[1] = 10    #dont support mutability
# numbers.append(5)
# numbers.remove(3)
# numbers.clear()

for num in numbers:
    print(num , end=" ")


# ---------------------------

#SETS
fruits = {"apple" , "banana" , "coconut" , "coconut" ,"coconut" } #no duplicates it handle only uniques

# fruits[1] =  "mango"   #no indexing changes can be done
# fruits.pop(0)

fruits.add("grapes")
fruits.remove("banana")
fruits.clear()

for fruit in fruits:
    print(fruit ,  end=" ") # gives different sequence output every time -> UNORDERED


# membership testing => means if there is given elm within that set
if "apple" in fruits:
    print("apple is founded in fruits sets")
else:
    print("apple not founded")