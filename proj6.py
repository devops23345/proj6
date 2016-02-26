# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:33:00 2016

@author: ncolella
"""

def rotate (str_input):
    
    str_rotated = "str_rotated"
    return str_rotated

def is_transpose (string1, string2):

    response = True
    
    return response

def get_transposability (input_number):
    print('get_transposability')
    return

def get_transposability_zero (input_number):
    print('get_transposability_zero')
    
    return
    
def open_file ():

    file_name_input = input("Enter filename::")

    while True:
        
        try: 
            fn = open(file_name_input, "r")
            
            break

        except FileNotFoundError:
            print ("Error:  No file found with name:", file_name_input)    
            print ("Try Again")
            file_name_input = input("Enter file name with extension:")    

    return fn
    
def process_file ():

    data_file = open_file()
    data_file.readline()## reads the first line which is the header. you can then start
    
    for line in data_file:
        
        # read start and end range
        # find 1st space to parse the start range
        first_space_index = line.find (" ")
        range_start = line[:first_space_index]
        range_end = line[first_space_index:]

        #range end is remaining value with the spaces stripped
        range_end = range_end.strip(" ")
        
        range_start = int(range_start)
        range_end = int(range_end)

        print ("Range Start =", range_start)
        print ("Range End =", range_end)
    
    for i in (10, 20):
#    for i in (range_start, range_end+1):
        
        print ('i=', i)
        
#        if i < 100000:# if less than 5 digits
#            get_transposability_zero(i)
#            
#        else:
#            get_transposability(i)
            
    return 


# Main Code
process_file()







#def squares( start, num ):
#    """Handles the squares function"""
#    sum = 0    
#    for i in range(start, start+num):
#        print('factor =', i)    
#
#        sum = sum + i**2
#        print('Sum =', sum)    
#        
#    return sum
#
#def cubes( start, num ):
#    """Handles the cubes function"""
#    print('cubes')
#    sum = 0    
#    for i in range(start, start+num):
#        print('factor =', i)    
#
#        sum = sum + i**3
#        print('Sum =', sum)    
#        
#    return sum
#
#    return 0
#
#
#input_cmd = input_cmd.lower()
#
#
#if input_cmd == "exit":
#    print('Exit')
#    
#elif input_cmd == "squares":
#    #do squars
#
#    squares_start = input('Enter start value:')
#    squares_start = int(squares_start)
#    squares_num = input('Enter number of factors:')
#    squares_num = int(squares_num)
#    print('Squares =', squares(squares_start,squares_num))
#
#elif input_cmd == "cubes":
#    #do cubes
#    cubes_start = input('Enter start value:')
#    cubes_start = int(cubes_start)
#    cubes_num = input('Enter number of factors:')
#    cubes_num = int(cubes_num)
#    print('Cubes =', cubes(cubes_start,cubes_num))
#else: 
#    print('*** Invalid choice ***')


