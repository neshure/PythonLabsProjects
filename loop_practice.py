# using zip to loop over list
# name = ['chioma', 'emma', 'oyinye']
# score = ['20', '30', '40']

# x = []
# for name, score in zip(name, score):
#     x.append(f'{name}:{score}')
# print(x)

#------------------------------------------------------------------------------------------#

#Use	setattr to set attribute of a var
# class Person:
# 	pass

# person = Person()

# person_dict = {
#     'first': 'John',
#     'last': 'Doe'
# }
# for key, value in person_dict.items():
# 	setattr(person, key, value)

# print(person.first)
#------------------------------------------------------------------------------------------#
# hidding PASSWWORD when using input function

# from getpass import getpass

# username = input('Enter username: ')
# password = getpass('enter password: ')

#------------------------------------------------------------------------------------------#

# Print the following pattern
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5 

#print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
# row = 5
# # start: 1
# # stop: row+1 (range never include stop number in result)
# # step: 1
# # run loop 5 times
# for i in range(1, row + 1, 1):
#     # Run inner loop i+1 times
#     for j in range(1, i + 1):
#        print(j, end=' ')
#     # empty line after each row
#     print("") 
# #-----------------------------------------------------------------#

#Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# number = 0

# for num in range(1, 10+1, 1):
#    number += num

# print(number)
#-----------------------------------------------------------------#
# Write a program to print multiplication table of a given number
# n = 3
# for i in range(2, 11, 1):
#     i = i * n
#     print(i)

#-----------------------------------------------------------------#

# numbers = [12, 75, 150, 180, 145, 525, 50]

# for num in numbers:
#     if num > 500: #If the number is greater than 500, then stop the loop
#         break
#     elif num > 150: #if the number is greater than 150, then skip it and move to the next number
#         continue
#     elif num % 5 == 0: #The number must be divisible by five
#         print(num)


#-----------------------------------------------------------------#
# # Write a program to use for loop to print the following reverse number pattern
# '''
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

# '''
# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()
   
#-----------------------------------------------------------------#
# Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]
# m = reversed(list1)

# for num in m:
#     print(num)
#-----------------------------------------------------------------#
#Display numbers from -10 to -1 using for loop

# for num in range(-10, 0, 1):
#     print(num)
