#!/usr/bin/env python3

#################################################
#
# Name : Nasser Binshabeeb, Michael Shaw
# Group : Liverpool
#
#
#################################################


import sys

#Code tables, a simple comprehension prefectly flips the tables

transTable = [ (0 , '||:::'),(1 , ':::||'), (2, '::|:|') ,
            (3 , '::||:'),(4 , ':|::|'),(5 , ':|:|:'),(6 , ':||::'),
            (7 , '|:::|'),(8 , '|::|:'),(9 , '|:|::') ]

reverseTable = dict([ (i[1],i[0]) for i in transTable])


def print_digit(d,callerID=0):
    """
    Prints digit/digits as a barcode
    Param:
        d: a string of any length of digits.
        callerID: defaulted to 0 (outside calls),
        to handle it differently when called from outside 
        or inside the script.
    Return:
        None
    """
    if callerID == 1:
        for i in d:
            print(transTable[int(i)][1], end='' )
    else:
        for i in d:
            print(transTable[int(i)][1], end='' )
        print('')



def print_barcode(zipCode):
    """
    Calls print_digit and prints the entire barcode after validation it
    also calls the check_sum to print that too
    Param:
        zipCode: input as 5 digits
    Return:
        None
    """
    
    t = transTable
    if zipCode.isdigit():
        if len(zipCode) == 5:
            print('|',end='')
            print_digit(zipCode,1)
            print(t[check_sum(zipCode)][1]+'|')
        else:
            print("Zip is not of length 5")
    else:
        print("Zip is not all numeric")



def check_sum(zipCode):
    """
    This function calculates the check sum, which is a number such that
    if it is added to to the sum of the zipcode digits, makes a number that
    is a multiple of 10.
    Param: 
        zipCode, used to get the sum of its digits
    Return:
        the check sum, calculated by the formula
    """
    toList = [ int(i) for i in zipCode ]
    return (10 - sum(toList)) % 10
    


#Main Function
def main():
    """
    Main function

    will call other functions in the module
    """


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)

#exit(0)
