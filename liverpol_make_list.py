#!/usr/bin/env python3

#################################################
#
# Name : Nasser Binshabeeb
# 
#
# Project Info : Python
#
#
#################################################


import sys
from urllib.request import urlopen 

def csv_to_list(url):
    """
    Opens the data file, reads it, and returns a list
    Args:
        url: the url where the file is
    Returns:
        dataList : a list that went through some filtering
    """
    
    #dataList will hold a list of all the data in the csv file
    dataList = []
    
    #Open the .csv file and extract the contents and filter them
    with urlopen(url) as wholeFile:
        for line in wholeFile:
            holderList = line.decode('UTF-8')[:-1].split(',')
            dataList.append(holderList)
    #delete first row
    del dataList[0]

    return dataList





#Main Function
def main():
    """
    Main function
    """
    url ="http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv"
    csv_to_list(url)



if __name__ == "__main__":
    # Call Main
    main()

    exit(0)



#exit(0)

