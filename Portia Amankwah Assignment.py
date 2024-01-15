#!/usr/bin/env python
# coding: utf-8

# Exercise 1
# What is the output of the following print statements?

# In[7]:


print("\ta\tb\tc") 


# In[8]:


print("\\\\")


# In[9]:


print("'")


# In[10]:


print("\"\"\"")


# In[11]:


print("C:\nin\the downward spiral")


# 2.	Write a print statement to produce this output:
# / \ // \\ /// \\\
# 

# In[12]:


print ('/ \ // \\\\ /// \\\\\\')


# 3.	What print statements will generate this output?
# This quote is from Irish poet Oscar Wilde:
# "Music makes one feel so romantic
# 
# - at least it always gets on one's nerves – which is the same thing nowadays."
# 

# In[26]:


print('This quote is from Irish poet Oscar Wilde:\n"Music makes one feel so romantic\n-at least it always gets on one\'s nerves–\n which is the same thing nowadays."')


# 4.	What print statements will generate this output?
# A "quoted" String is 'much' better if you learn
# the rules of "escape sequences." Also, "" represents an empty String. Don't forget: use \" instead of " ! '' is not the same as "
# 

# In[32]:


print('A \"quoted"\ String is\n\'much\' better if you learn \nthe rules of \"escape sequences.\" \nAlso, \"\" represents an empty String. \nDon\'t forget: use \\\" instead of \" ! \n\'\' is not the same as "')


# 5.	What values result from the following expressions?

# In[1]:


9 / 5


# In[2]:


695 % 20


# In[3]:


7 + 6 * 5


# In[4]:


7 * 6 + 5


# In[5]:


248 % 100 / 5


# In[6]:


6 * 3 - 9 / 4


# In[7]:


(5 - 7) * 4


# In[8]:


6 + (18 % (17 - 12))


# Exercise 2
# Write a program that finds the maximum value of the given list, assuming that the list
# contains at least one element.

# In[9]:


my_list = [2, 4, 7, 4, 23, 5, 1, 4, 8, 9]
max(my_list)


# Write a program that calculates the average value of the given list.

# In[15]:


#using sum and len
my_list2 = [4, 7, 1, 5, 11, 53, 12, 46, 84, 23]
sum(my_list2)/len(my_list2)


# Write a program that prints the given list of integers in reverse order

# In[27]:


my_list3 = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]

for i in range(len(my_list3)-1,-1,-1):
    print(my_list3 [i])


# Write a program that accepts two lists of integers and prints true if each element in the first
# list is less than the element at the same index in the second list. Your program should print
# false if the lists are not the same length

# In[38]:


list1 = [2, 3, 5, 9, 13]
list2 = [1, 2, 3, 4, 5]
if list1 < list2:
    print ("True")
else:
    print ("False")


# Write a program that accepts a list of integers and two indexes and swaps the elements at
# those indexes

# In[42]:


def swap_index(num_list, index_1, index_2):
    if 0 <= index_1 < len(num_list) and 0 <= index_2 < len(num_list):
        num_list[index_1], num_list[index_2] = num_list[index_2], num_list[index_1]
        print(num_list)
    else: 
        print("invalid input")
    return
test_list = [5, 8, 2, 4, 10, 24, 19, 44, 98, 16 ]
result = swap_index(test_list, 5, 6)


# Write a program that accepts two lists of integers and prints a new list containing all
# elements of the first list followed by all elements of the second

# In[43]:


def merge_list(list1, list2):
    new_list = list1 + list2
    
    return new_list
list_1 = [5, 7, 1, 9, 21, 64, 8, 23, 4, 16 ]
list_2 = [3, 6, 7, 15, 38, 29, 19, 45, 89, 5 ]
result = merge_list(list_1, list_2)
print(result)


# Write a program that accepts a list of integers and an integer value as its parameters and
# prints the last index at which the value occurs in the list. The program should print –1 if the
# value is not found.

# In[74]:


def find_last_index(list7, value):
    try:
        return len(list7) - 1 - list7[::-1].index(value)
    except ValueError:
        return -1

print(find_last_index([74, 85, 102, 99, 101, 85, 56], 85))  


# Write a program that prints the range of values in a list of integers. The range is defined as 1 more than the difference between the maximum and minimum values in the list. For example, if a list contains the values 36, 12, 25, 19, 46, 31, 22], the program should return 35. You may assume that the list has at least one element.

# In[75]:


def print_range(list8):
    if not list8:
        return "List is empty"
    range_value = max(list8) - min(list8) + 1
    return range_value

# Testing the  output
print(print_range([36, 12, 25, 19, 46, 31, 22])) 


# Write a program that accepts a list of integers, a minimum value, and a maximum value and
# prints the count of how many elements from the list fall between the minimum and
# maximum (inclusive).

# In[45]:


def count_betw(lst, mini, maxi):
    count = 0
    for x in lst:
        if mini <= x <= maxi:
            count = count + 1
    return count
    

list_1 = [8, 7, 6, 3, 16, 22, 18, 5, 24, 34]
min_value = 1
max_value = 20
result = count_betw(list_1, min_value, max_value )
print(result)


# Write a program that accepts a list of real numbers and prints true if the list is in sorted
# (nondecreasing) order and false otherwise.

# In[46]:


def sort_list(lst):
    sorted_list = sorted(lst, reverse = True)
    
    return sorted_list
list_1 = [5, 8, 2, 14, 17, 44, 11, 6, 37, 28]
result = sort_list(list_1)
print(result)


# Exercise 3
# Write a program to produce the following output using for loop
# +----+
# \ /
# / \
# \ /
# / \
# \ /
# / \
# +----+

# In[48]:


for x in range(5):
    if x == 0 or x == 4:
        print("+----+")
    else:
        print("\\    /")
        print("/    \\")


# Write a program to produce the following output using for loop
# **********
# **********
# **********
# **********
# **********

# In[49]:


for i in range(5):
    print('**********')


# Complete the code for the following for loop:so that it prints the following numbers, one per line:

# In[51]:


for i in range(1,7):
    a = i
    b = i * 2
    c = i * 15 - 11
    d = 40 - 10 * i
    e = 4 * i - 11
    f = 97 - 3 * (i - 1)
    g = (18 * (i - 1)) - 4
    print(a, b, c, d, e, f, g)


# Write a program to produce the following output using for loops. Then
# use a class constant to make it possible to change the number of lines in
# the figure.

# In[52]:


class Figure:
    NUM_LINES = 7  
    
    @classmethod
    def print_figure(cls):
        for i in range(1, cls.NUM_LINES + 1):
            for j in range(i):
                print(i, end="")
            print()
Figure.print_figure()


# Write a method named pay that accepts two parameters: a real number
# for a TA's salary, and an integer for the number of hours the TA worked
# this week. The method should return how much money to pay the TA.

# In[53]:


def pay(salary, hours_worked):
    normal_hours = min(8, hours_worked)
    overtime_hours = max(0, hours_worked - 8)
    overtime_rate = 1.5

    total_payment = (normal_hours * salary) + (overtime_hours * salary * overtime_rate)
    return total_payment


result = pay(5.50, 6)
print(result)  

result = pay(4.00, 11)
print(result)


# Consider the following method for converting milliseconds into days:

# In[56]:


import math

def area(radius):
    return math.pi * radius ** 2

# Example usage:
radius = 2.0
result = area(radius)
print(result)


# Copy and paste the following code into pythons IDLE script
# environment.

# In[59]:


low = int(input("low? "))
high = int(input("high? "))
sum_result = 0

for i in range(low, high):
    sum_result += i

print("sum =", sum_result)


# Write a program using while loop that prompts the user for numbers until
# the user types 0, then outputs their sum.

# In[60]:


total_sum = 0

while True:
    user_input = input("Enter a number (type 0 to stop): ")
    
    if user_input == '0':
        break
    
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Sum of the numbers: ", total_sum)


# Write a program using while loop that prompts the user for numbers until
# the user types -1, then outputs their sum.

# In[63]:


total_sum = 0

while True:
    user_input = input("Enter a number (type -1 to stop): ")
    
    if user_input == '-1':
        break
    
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
    print("Sum of the numbers: ", total_sum)


# Write a method named repl that accepts a String and a number of repetitions as parameters and returns the String concatenated that many times. 

# In[67]:


def repl(s, repetitions):
    if repetitions <= 0:
        return ""
    else:
        return s * repetitions


result = repl("Hello ", 3)
print(result) 


# Write a method called printRange that accepts two integers as arguments and prints the sequence of numbers between the two arguments, separated by spaces. Print an increasing sequence if the first argument is smaller than the second; otherwise, print a decreasing sequence. If the two numbers are the same, that number should be printed by itself.

# In[71]:


def printRange(start, end):
    if start < end:
        for i in range(start, end + 1):
            print(i, end=" ")
    elif start > end:
        for i in range(start, end - 1, -1):
            print(i, end=" ")
    else:
        print(start)


printRange(2, 7)

printRange(19, 11)

printRange(5, 5)


# Write a method named smallestLargest that asks the user to enter numbers, then prints the smallest and largest of all the numbers typed in by the user. You may assume the user enters a valid number greater than 0 for the number of numbers to read.

# In[ ]:




