# ---Numeric Data--- #

# num = 3
# num2 = 3.14
# print(num)
# print(type(num))

# print(num2)
# print(type(num2))

# --- Variables--- #

# my_variable = 10
# total_count = 0
# user = 'John'

# --- Operators --- #
# x = 10
# y =2

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(5%2)
# print(x**y)

# x += 2
# print(x)
# x -=2
# print(x)

# --- Operators with String --- #

# str1 = 'Hello'
# str2 = 'World'
# print(str1 + " " + str2 + " " + str2)
# print(str1 * 3)

# --- Control Statements --- #

# #num = 10 
# num = -5
# if num > 0:
#     print("This number is positive")
# elif num == 0:
#     print("This number is zero")
# else:
#     print("This number is negative")

# num1 = int(input("Enter the first number"))
# num2 = int(input("Enter the second number"))

# --- Control Statements Part 2 --- #
# if num1 > num2:
#     print(num1, "is greater than", num2)
# elif num2 > num1:
#     print(num2, "is greater than", num1)
# else:
#     print("Both numbers are equal")

# --- Loops --- #

# fruit = ["apple","banana","cherry"]
# for fruit in fruit:
#     print(fruit)

# numbers = [1, 2, 3, 5, 7]
# for number in numbers:
#     print(number)

# count = 1

# while count <= 5:
#     print(count)
#     count += 1 # Increments the count by 1

# --- Loops Control Statements --- #

fruits = ["apple","banana","cherry","date"]
for fruit in fruits:
    if fruit == "cherry":
        break # Exits the loop if cherry is found
    print(fruit)
    
print()
    
for fruit in fruits:
    if fruit == "cherry":
        continue # Skips cherry and moves to the iteration
    print(fruit)

print()
    
for fruit in fruits:
    if fruit == "cherry":
        pass # placeholder, no action is needed for cherry
    print(fruit)
    
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break # Exits the loop when the count is reached - 3
