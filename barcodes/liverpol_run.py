#!/usr/bin/env python3


#################################################
#
# Name : Nasser Binshabeeb, Michael Shaw
# Group : Liverpool
#
#
#################################################


import sys
from urllib.request import urlopen
import liverpol_defs


def proc_data(url):
    """
    takes input from the url, and calls the imported functions from the
    other modules to complete the task. A very basic exception is handled
    to alert us that the task has failed by any means.
    The function Then starts an input loop for the user to input more
    zipCodes manually.
    Params:
        url: source of the test file
    Return:
        None
    """
    try :
        with urlopen(url) as theFile:
            print("****** Test File ******")
            for line in theFile:
                print("Zipcode:",line.decode("UTF-8").strip())
                liverpol_defs.print_barcode(line.decode('UTF-8').strip())
                print('')
        print("****** End Test File ******")
    except:
        print("Failed to open the Test file, check the file path")

    finally:
        while True:
            print("Enter a zipcode (q to quit) :")
            userInput = input()
            if userInput.lower() == 'q':
                break
            liverpol_defs.print_barcode(userInput)
            print('')


def help():
    """
    Help function:
    Args: None
    Return: None
    """
    
    print("Help function")
    print("bash Usage: ./liverpol_run.py <url>")
    print("Hint: http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt")
    print("python3 Usage: liverpol_run ")
    print("then call liverpol_run.main(url)")
    exit(1)


#Main Function
def main():
    """
    Main function
    this will call proc_data(url) , taking the user's url 
    """
    if len(sys.argv) > 1 :
        url = sys.argv[1]
    else:
        url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt"
    proc_data(url)

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)

#exit(0)
