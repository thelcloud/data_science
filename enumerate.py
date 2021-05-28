#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 22:11:30 2021

@author: handey
"""

def alternating(string):
    new_string=""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
         
            
    print(new_string)
    
    
    
alternating("hi my name is hande and i am learning python")    


####################################################################

students = ["Hande","Cansu","Sahine","Nihat"]

def divide_students(students):
    groups = [[],[]]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
            
    print(groups)
    
divide_students(students)    


####################################################################



def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
            
        else:
            new_string += letter.lower()
            
    print(new_string)
    
alternating_with_enumerate("hi my name is hande and i am learning python")    