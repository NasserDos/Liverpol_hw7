#!/user/bin/env python3
import sys
import re
import argparse
from urllib.request import urlopen
import csv

def download_file():

    """
    Downloads the .csv file an reads into an empty array, function is called by main when executed
    """

    store_file = [] # Empty array to store the data from the csv file

    # using open to get the .csv file on the icarus server
    with open('icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv', 'r') as url:
        reader = csv.reader(url)
        my_list = list(reader)
    print(my_list)
    print(my_list[0])

# these next lines are to append and store in an array
        # next(url) # Skipt he header colums
        # loop throgh the data and append it to a variable for printing out
  #  for i in url:
   #     store_file.append(i)
    #    print(i)

def main():
    """
    Main function
    """
    download_file()

    pass

if __name__ == "__main__":
    #call main fuction
    main()

    exit(0)

