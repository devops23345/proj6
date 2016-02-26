# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:33:00 2016

@author: ncolella
"""

def rotate (str_input):
    
    end_digit = str_input[5:6]
    first_5_digits = str_input[:5]
#    print ('end_digit=', end_digit)
#    print ('first_5_digits=', first_5_digits)

    str_rotated = end_digit+first_5_digits
#    print ('str_rotated=', str_rotated)

    return str_rotated

def is_transpose (string1, string2):
    response = False
    count = 1

    while response == False:

        if string1 == string2:
            response = True
            
            break

        else:
            
            if count < 6:    
        
                string2 = rotate(string2)
                count = count + 1
            else:#not transposable
                break


    return response

def get_transposability (input_number):
    check_transpose = False
    
    string_1 = str(input_number)
       
#    print ('string_1=', string_1)
    
    for i in range(2, 10):
        string_2 = input_number * i

        if string_2 > 1000000:
            continue

        string_2 = str(string_2)

#        print ('string_2=', string_2)
            
        check_transpose = is_transpose(string_1, string_2)
        
        if check_transpose == True:
            print (string_1 + " * " + str(i) + " = " + string_2)            
            
    return

def get_transposability_zero (input_number):
#    print('get_transposability_zero')
    check_transpose = False
    
    string_1 = str(input_number)
    string_1 = "0"+string_1
       
#    print ('string_1=', string_1)
    
    for i in range(2, 10):
        string_2 = input_number * i

        if string_2 < 100000:
            string_2 = "0"+str(string_2)
        elif string_2 > 1000000:
            continue
        else:
            string_2 = str(string_2)

#        print ('string_2=', string_2)
            
        check_transpose = is_transpose(string_1, string_2)
        
        if check_transpose == True:
            print (string_1 + " * " + str(i) + " = " + string_2)            
            
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
    
    for i in range(range_start, range_end+1):
        
        
        if i < 100000:# if less than 5 digits
            get_transposability_zero(i)
            
        else:
            get_transposability(i)
            
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


