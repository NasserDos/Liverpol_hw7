# Liverpol_hw7
Python assignment HW7

### **minivan Modules:** ./liverpol_process_data.py
1) liverpol_make_list.py : will read the csv file and return a list. Contains definitions such as csv_to_list(url) that handles the input file

2) liverpol_process_data.py : will import the first module and perform some logical operations to find the result. Contains definitions such as process_data(data) which takes a list, and fancy_print(aList) which prints the results from a list.


### **barcodes Modules:** ./liverpol_run.py
1) liverpol_defs.py: has the definitions needed to complete the task. Contains print_digit(d) , which takes a string of integers and prints it as barcode. it also contains print_barcode(zipCode), which calls print_digit(d) after some input validation, and it also calls check_sum(zipCode) which calculates the check sum .


2) liverpol_run.py: This module imports the liverpol_defs.py module and opens a test file to test the modules. It contains definitions such as proc_data(url), which takes an input file, and runs it through the modules to test the modules.
