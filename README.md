# Liverpol_hw7
Python assignment Mod4 HW7

# ############################ START TASK1 OUTLINE ########################################

# TASK: to simulate a portion of the control software for the vehicle door(s) locks.

# A minivan has two sliding doors. Each door can be opened by either a dashboard switch, it’s
# inside handle, or its outside handle. However, the inside handles do not work if a child lock
# switch is activated. In order for the sliding doors to open, the gear shift must be in park, and the
# master unlock switch must be activated. 

# Module 1:
#		########## Create lists to hold data for: ##########

#			Set dashboard switches for left and right sliding door, child lock, and 
#				master unlock (0 for offand/or 1 for activatii 
#			set inside and outside handles on the left and right sliding doors (0 or 1)
# 			Set the gear shift setting (one of P N D 1 2 3 R).
#			

#				#### DATALIST ####
#      		dataList will hold a list of all the data in the csv file
#			dataList = []
#
#			Open the .csv file and extract the contents and filter them
#			with urlopen(url) as wholeFile:
#				for line in wholeFile:
#					holderList = line.decode('UTF-8')[:-1].split(',')
#					dataList.append(holderList)
#

#					 
#			del dataList[0] #delete first row
#
#			return dataList #return the list
#				#### END DATALIST ####

# Module 2:
#		########## Import the first module for tesing input file ##########
#
#				#### PROCESS DATA ####
#
#		Gears = [' P',' R',' N',' D',' 1',' 2',' 3']
#		outcome = ['Both doors stay closed','Right door opens.','Left door opens.','Both doors open.',"Invalid Record: Both doors stay closed"]
#   
#		for setting in data:#for each entery
#			lDoor = 0 #prepare door variables
#			rDoor = 0
#			if setting[9] in Gears: #validate gear
#				if setting[9] == ' P' and int(setting[4]): #P on? master?
#					if not int(setting[3]): #Child lock
#						rDoor = int(setting[7]) #right inside
#						lDoor = int(setting[5]) #left inside
#	
#						#left dash          left outside
#					 lDoor = int(setting[1]) | int(setting[6]) | lDoor
#
#						#right dash         right outside
#					rDoor = int(setting[2]) | int(setting[8]) | rDoor
#
#					if rDoor:
#						result = 1
#					if lDoor:
#						result = 2
#					if lDoor and rDoor:
#						result = 3
#
#				else:
#					result = 0 #gear is not P
#							  
#			else:
#				result = 4 #Invalid input
#
#			fancy_print(setting)    #print the whole setting
#			print(outcome[result])  #print the outcome
#			print("***************************************************")
#
#					#### End Process Data ####

#			Input file contains the following Information:
#				H1, LD, RD, CL, ML, LI, LO, RI, RO, GS
#				R1, 0, 0, 0, 1, 0, 1, 0, 0, P
#				R1, 0, 1, 0, 1, 0, 1, 0, 0, P
#				R1, 1, 0, 0, 1, 0, 1, 0, 0, D
#				R1, 1, 0, 0, 1, 0, 1, 0, 0, R

#			Print header record (H1) with the following fields:
#				Left dashboard switch (LD)
#				Right dashboard switch (RD)
#				Child lock switch (CL)
#				Master unlock switch (ML)
#				Left inside handle (LI)
#				Left outside handle (LO)
#				Right inside handle (RI)
#				Right outside handle (RO)
#				Gear shift position (GS): Valid Fields: P, N, D, 1, 2, 3 or R

# ########################## END TASK 1 ################################################



# ######################## START TASK 2 ################################################

#	Use the encoding scheme provided for a five-digit zip code. There are full-height
#		frame bars on each side. The five encoded digits are followed by a check digit, which is

#	computed as follows:
#		1. Add up all digits
#		2. Choose the check digit to make the sum a multiple of 10.

#		For example, the zip code 95014 has a sum of 19, so the check digit is 1 to make the sum
#			equal to 20
#			Each digit in the zip code, and the check digit, is encoded according to the table below,
#	 		where 0 denotes a half bar and 1 denotes a full bar.

#	 		The digit can be easily computed from the bar code using the column weight 7, 4, 2, 1, 0.
#			Example, 01100 is 0*7 + 1*4 + 1*2 + 0*1 + 0*0 = 6. The only exception is 0, which
#				would yield 11 according to the weight formula. 

#  Module 3:
#		########## Create functions to print ##########
#	 		Create a function to print the digits: def printDigit(d)
#	 		Create a second  function to print the bar code: def printBarCode(zipCode)

#  Module 4:
# 		########## Import third module for digit transformation  ########
#
#			This second module will import the third module, and it will transform the zip code 
#				numbers from a file. 
# 			The input file is located in the following url: 
#				www.icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt 
#
# ######################## END TASK 2 ###################################################
