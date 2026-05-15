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
        return str(choice)
    elif choice == 9:
        return str(choice)
    else:
        print("Invalid Choice, Try Again!")
        inputMenu()

def enterCustomerInfo(postal_codes):
    
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    city = input("What is your city: ")

    postal_code = enterPostalCode()
    if not validatePostalCode(postal_code, postal_codes):
        print("Not a valid Canadian postal code")
        return
    else:
        pass

    while True:
        card_num = input("Please enter your credit card number: ")
        if not validateCreditCard(card_num):
            print("Invalid credit card number. Try again.")
            continue
        else:
            break

    return [first_name, last_name, city, postal_code, card_num]

    



'''
    Entering/Validating Postal Code
'''

# Entering Postal Code
def enterPostalCode():
    valid_postal_code = False

	# Used to stop complete break out of function
    while True:
    	# Keeps looping until proper postal code
        while valid_postal_code == False:
            enter_postal_code = input("Postal Code: ")

            # Checks if input length is not 3
            if len(enter_postal_code) != 6: 
                print("Input proper length (6)")
                continue

            # Continues if input length is 3
            else:
                break_loop = False
                for x in range(len(enter_postal_code)):
                    
                    # Checks if character is a digit or letter in correct position
                    if (x % 2 == 0 and enter_postal_code[x].isalpha() == True) or (x % 2 == 1 and enter_postal_code[x].isdigit() == True): 
                        continue

					# If character not correct, breaks out of for loop
                    else:
                        print("Input proper postal code.")
                        valid_postal_code = False
                        break_loop = True
                        break

				# Returns to while loop for new postal code input if character not correct
                if break_loop == True:
                    break
				
                # Returns postal code if valid
                return enter_postal_code
		
# Checks if first 3 characters in PostalCode are in files
def validatePostalCode(PostalCode, postal_codes):
    if PostalCode[:3].upper() in postal_codes: 
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
def generateCustomerDataFile(customer_data):
    
    file_name = input("What would you like the file name to be (no extension): ")
    file_name = file_name + ".csv"
    
    contents = "id, first_name, last_name, city, postal_code, credit_card\n"
    for user in customer_info:

        for index, item in enumerate(user):
            user[index] = str(item)

        user_string = ",".join(user) + "\n"
        contents += user_string

    with open(file_name, "w") as fp:
        fp.write(contents)

    return file_name

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

# [id, first_name, last_name, city, postal_code, credit_card]

with open("postal_codes.csv", "r") as csv_codes:
    postal_codes = [(line.split("|")[0]) for line in csv_codes.read().split("\n")]
del postal_codes[-1]

customer_info = []

while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = inputMenu();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be edited based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        user_info = enterCustomerInfo(postal_codes)
        user_info.insert(0, len(customer_info) + 1)
        customer_info.append(user_info)


    elif userInput == generateCustomerOption: 
            # Only the line below may be edited based on the parameter list and how you design the method return
        file_name = generateCustomerDataFile(customer_info)
        print(file_name)

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")
