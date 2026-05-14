# CxId (generated),Firstname,Lastname,DOB,Address,Postal Code (valid) ,Credit Card (valid)


# Throughout this project, the use of data structures are not permitted (lists allowed)
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor

def printMenu():
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          ''')


'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''

def inputMenu():
    choice = int(input("Enter menu option (1-9)"))
    if choice in range(1,5):
        match choice:
            case 1:
                enterCustomerInfo()
            case 2:
                generateCustomerDataFile()
            case 3:
                # report on total sales
                pass
            case 4:
                # check for fraud in sales data
                pass
            case _:
                pass
    elif choice == 9:
        print("Thank you for using the program!")
        quit()
    else:
        print("Invalid Choice, Try Again!")
        inputMenu()

def enterCustomerInfo():
    pass    # Remove this pass statement and add your own code below

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''

def enterPostalCode():
	valid_postal_code = False
	while valid_postal_code == False:
		enter_postal_code = input("Postal Code: ")
		if len(enter_postal_code) != 3:
			return
		

def validatePostalCode(PostalCode, csv_file):
    if PostalCode[:3] in postal_codes: 
        return True
    else:
        return False
    

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validateCreditCard(card):
    # Must be exactly 16 digits
    if len(card) != 16 or not card.isdigit():
        return False

    total = 0

    # Luhn Algorithm
    for idx, char in enumerate(card):
        digit = int(char)

        # Double every second digit from the left
        if idx % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9

        total += digit

    return total % 10 == 0


	


'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def generateCustomerDataFile():
    pass    # Remove this pass statement and add your own code below

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################




####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below

with open("postal_codes.csv", "r") as csv_codes:
    postal_codes = [(line.split("|")[0]) for line in csv_codes.read().split("\n")]
del postal_codes[-1]


while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = inputMenu();        # User selection from the menu

    if userInput == enterCustomerOption:
            # Only the line below may be edited based on the parameter list and how you design the method return
            # Any necessary variables may be added to this if section, but nowhere else in the code
            enterCustomerInfo()

    elif userInput == generateCustomerOption: 
            # Only the line below may be edited based on the parameter list and how you design the method return
        generateCustomerDataFile()

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")
