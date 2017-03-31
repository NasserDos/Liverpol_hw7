#!/usr/bin/env python3

#################################################
#
# Name : Nasser Binshabeeb, Michael Shaw
# Group : Liverpool
#
#
#################################################


import sys

#Code table

transTable = [ (0 , '||:::'),(1 , ':::||'), (2, '::|:|') ,
            (3 , '::||:'),(4 , ':|::|'),(5 , ':|:|:'),(6 , ':||::'),
            (7 , '|:::|'),(8 , '|::|:'),(9 , '|:|::') ]

reverseTable = dict([ (i[1],i[0]) for i in transTable])


def print_digit(d):
    """
    prints digits
    Param:
        d: input as barcode?
    Return:
        None
    """
    if d in reverseTable:
        print(reverseTable[d])
    else:
        print("Invalid digit was entered")
    



def print_barcode(zipCode):
    """
    prints the zipcode
    Param:
        zipCode: input as 5 digits
    Return:
        None
    """
    
    t = transTable
    if zipCode.isdigit():
        if len(zipCode) == 5:
            print('|'+t[int(zipCode[0])][1]+t[int(zipCode[1])][1]+
                    t[int(zipCode[2])][1]+t[int(zipCode[3])][1]+
                    t[int(zipCode[4])][1]+t[check_sum(zipCode)][1]+'|')
        else:
            print("Zip is not of length 5")
    else:
        print("Zip is not all numeric")





def check_sum(zipCode):
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

