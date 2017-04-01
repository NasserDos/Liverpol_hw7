#!/usr/bin/env python3

#################################################
#
# Names : Nasser Binshabeeb, Michael Shaw
# Group : Liverpool
#
#################################################

import sys
from liverpol_make_list import csv_to_list


def process_data(data):
    """
    Process the list containing the data
    Args:
        data: this will be the list imported from the other module
    Return:
        None
    """

    Gears = [' P',' R',' N',' D',' 1',' 2',' 3']
    
    outcome = ['Both doors stay closed','Right door opens.','Left door opens.','Both doors open.',"Invalid Record: Both doors stay closed"] 

    for setting in data:#for each entery
        lDoor = 0 #prepare door variables
        rDoor = 0
        if setting[9] in Gears: #validate gear
            if setting[9] == ' P' and int(setting[4]): #P on? master?
                if not int(setting[3]): #Child lock
                    rDoor = int(setting[7]) #right inside
                    lDoor = int(setting[5]) #left inside
                        
                        #left dash          left outside
                lDoor = int(setting[1]) | int(setting[6]) | lDoor

                        #right dash         right outside
                rDoor = int(setting[2]) | int(setting[8]) | rDoor 

                if rDoor:
                    result = 1
                if lDoor:
                    result = 2
                if lDoor and rDoor:
                    result = 3
            else:
                result = 0 #gear is not P
        else:
            result = 4 #Invalid input

        fancy_print(setting)    #print the whole setting
        print(outcome[result])  #print the outcome
        print("***************************************************")



def fancy_print(aList):
    """
    Prints the contents of a list of size 10
    Args:
        aList : the list in question
    Return:
        None
    """
    #output format
    print("Reading Record",aList[0][1],":")
    print("Left dashboard switch (0 or 1):",aList[1].strip())
    print("Right dashboard switch (0 or 1):",aList[2].strip())
    print("Child lock switch (0 or 1):",aList[3].strip())
    print("Master unlock switch (0 or 1):",aList[4].strip())
    print("Left inside handle (0 or 1):",aList[5].strip())
    print("Left outside handle (0 or 1):",aList[6].strip())
    print("Right inside handle (0 or 1):",aList[7].strip())
    print("Right outside handle (0 or 1):",aList[8].strip())
    print("Gear shift position (P, N, D, 1, 2, 3 or R):",aList[9].strip())



#Main Function
def main():
    """
    Main function

    Will call other functions in the module
    """


    dataList = csv_to_list("http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv")
    process_data(dataList)



if __name__ == "__main__":
    # Call Main
    main()

    exit(0)

#exit(0)
