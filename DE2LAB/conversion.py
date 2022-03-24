#!/usr/bin/env python3
import time

"""
    The implementation is used to demonstrate an intensive "conversion" function on elements
"""

# Fill in your author information
___author___ = ""
___email____ = ""

# Input string
INPUT_STRING = "I want to be capatilized"

# Iteration represents the operation applied to each word in the string 
# e.g., 1 represents that operation is applied to first word in the string
ITERATION = 5

def conversion(substring, operation):
    """A conversion function which takes a string as an input and outputs a converted string

    Args:
        substring (String)
        operation (function): This is an operation on the given input

    Returns:
        [String]: Converted String
    """


    # returns the conversion applied to input
    return function(substring)



def function(string):
    """ A function that performs some operation on a string. You can change the operation accordingly

    Args:
        string (String): input string on which some operation is applied

    Returns:
        [String]: string in upper case
    """
    return string.upper()





if __name__ == "__main__":

    # Check for correct input
    if ITERATION > len(INPUT_STRING.split()):
        print ("Iteration cannot be greater than the number of words in a string")
        print ("Terminating the benchmark")
        exit()

    print ("Original String: {}".format(INPUT_STRING))
    resultant_string = ""
    


    split_string = INPUT_STRING.split(" ")


    for i in range(0,ITERATION):

        upper_case_string = conversion(split_string[i], function)
        
        resultant_string +=   upper_case_string  + ' '    


    print ("Resultant String: {}".format(resultant_string))
