# A.
# 1.
X = 7
Y = 4

# 2.
if X > Y:
    print("BIG")

# 3.
elif X < Y:
    print("small")

# B.
# 1.
for i in range(5):
    # 2.
    print("Iteration number:", i + 1)

# C.
# 1.
season_variable = 3

# 2.
if season_variable == 1:
    print("summer")
elif season_variable == 2:
    print("winter")
elif season_variable == 3:
    print("fall")
elif season_variable == 4:
    print("spring")

# D.
# 1.
# The loop will run 10 times.
# 2.
# The loop will print numbers from 0 to 9, so the last printed number will be 9.

# E.
# Variables
age = 41
last_name_initial = 'C'
shekels_to_dollar = 3.5
abroad_flight = True
apartment_number = 18

# Print all variables
print("Age:", age)
print("Last name initial:", last_name_initial)
print("Shekels to Dollar rate:", shekels_to_dollar)
print("Flew abroad:", abroad_flight)
print("Apartment number:", apartment_number)

# Add currency to age
age_with_currency = age + shekels_to_dollar
print("Age with currency:", age_with_currency)

# F.
# 1.
phone_number = input("Enter your phone number: ")
# 2.
print("Phone number:", phone_number)

# G.
# 1.
def printHello():
    print("hello")

# 2.
def calculate():
    result = 5 + 3.2
    print("Result:", result)

# H.
# 1.
def printName(name):
    print("Name:", name)

# 2.
def divideByTwo(number):
    result = number / 2
    print("Result:", result)

# I.
# 1.
def addNumbers(a, b):
    return a + b

# 2.
def concatenateStrings(str1, str2):
    return str1 + ' ' + str2

# Challenges:

# K.
# Create a nested for loop for a pyramid shape
for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# L.
# Create a nested for loop for an X shape
for i in range(7):
    for j in range(7):
        if i == j or i + j == 6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# M.
# 1.
def getNumberFromUser():
    return int(input("Enter a number: "))

# 2.
def sumOfDigits(number):
    return sum(map(int, str(number)))

# Get number from user
user_number = getNumberFromUser()

# Compute and print the sum of digits
sum_result = sumOfDigits(user_number)
print("Sum of digits for", user_number, "is", sum_result)
