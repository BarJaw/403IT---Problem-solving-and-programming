# # Exercise 1
# number = int(input())
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")

# # Exercise 2
# number = int(input())
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

# # Exercise 3
# var = int(input())
# if isin(var) == str:
#     print("string")
# elif type(var) == int:
#     print("integer")

# # Exercise 4
# string = input()
# if string.isnumeric():
#     print("string is numeric")
# else:
#     print("string isn't numeric")

# # Exercise 5
# height = float(input())
# weight = float(input())
# bmi = weight / (height ** 2)
# print(bmi)

# # Exercise 6
# for i in range(1, 101, 2):
#     print(i)

# # Exercise 7
# numbers = [int(number) for number in input().split()]
# even_count = 0
# odd_count = 0
# for number in numbers:
#     if number % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(even_count, odd_count)

# # Exercise 8
# word = input()
# print(word[::-1])

# # Exercise 9
# def celsius_to_fahrenheit(degrees):
#     return degrees * (9 / 5) + 32

# # Exercise 10
# def contains(numbers, certain_number):
#     if certain_number in numbers:
#         return True
#     return False

# # Exercise 11
# password = "123"
# while input() != password:
#     print("Incorrect")
# print("Correct")

# # Exercise 12
# grade = float(input()[:-1])
# if grade >= 70:
#     print('1st class')
# elif grade >= 60:
#     print('2:1')
# elif grade >= 50:
#     print('2:2')
# elif grade >= 40:
#     print('3rd class')
# else:
#     print('Fail')

# Exercise 13
# i = 1.0
# while i <= 2.0:
#     print(round(i, 2))
#     i += 0.01


# # Exercise 14
# import random
# random_number = random.randint(0, 10)
# while int(input()) != random_number:
#     print("wrong")
# print("correct")

# # Exercise 15
# numbers = [print(number, end=' ') for number in input().split() if int(number) % 2 != 0]
# print()

# # Exercise 16
# string = input()
# if string[::-1] == string:
#     print("Palindrome")
# else:
#     print('Not a palindrome')

# # Exercise 17
# list_1 = [number for number in input().split()]
# list_2 = [number for number in input().split()]
# for i in range(len(list_1)):
#     if list_1[i] in list_2:
#         print(list_1[i])

# # Exercise 18
# first_name = input()
# last_name = input()
# print(last_name, first_name)

# # Exercise 19
# filename = input()
# print(filename[filename.index('.') + 1:])

# # Exercise 20
# import re
# password = input()
# x = re.search(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{6,16}', password)
# if x:
#     print("Valid password")
# else:
#     print('Invalid password')

# # Exercise 20v2
# from string import ascii_lowercase, ascii_uppercase
# password = input()
# lowercase = False
# uppercase = False
# digit = False
# special = False
# special_chars = ['$', '#', '@']
# if len(password) >= 6 and len(password) <= 16:
#     for char in password:
#         if char in ascii_lowercase:
#             lowercase = True
#         elif char in ascii_uppercase:
#             uppercase = True
#         elif char.isnumeric():
#             digit = True
#         elif char in special_chars:
#             special = True
# if lowercase and uppercase and digit and special:
#     print("Valid password")
# else:
#     print("Invalid password")



# # Exercise 21
# months_and_days = {
#     'January' : 31,
#     'February' : '28/29',
#     'March' : 31,
#     'April' : 30,
#     'May' : 31,
#     'June' : 30,
#     'July' : 31,
#     'August' : 31,
#     'September' : 30,
#     'October' : 31,
#     'November' : 30,
#     'December' : 31
# }
# month = input()
# print("No. of days:", months_and_days[month])

# # Exercise 22
# for i in range(9):
#     print(str(i + 1) * (i + 1), end = '')
#     print()

# # Exercise 23
# j = 5
# for i in range(9):
#     if i <= 4:
#         print('*' * (i + 1), end='')
#     else:
#         print('*' * j, end='')
#         j -= 1
#     print()