# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file. Simple code to check palindrome or not
Created on Wed June 24 10:56:13 2018

@author: prithvisekhp
"""

def palindromCheck(inputUser):
    array = []
    palindrome_input = inputUser
    divide2 = len(palindrome_input)
    input_size = len(palindrome_input)
    counter = 0
    for j in range(input_size):
        array.append(palindrome_input[j])
    size_array = len(array)
    for i in range(divide2):
        if array[i] != array[size_array-1-i]:
            counter = counter + 1
    if counter == 0:
        print("It's a palindrome\n")
        return 1
    else:
        print("It's not a palindrome\n")
        return 0
#assert palindromCheck('aba') == 1
