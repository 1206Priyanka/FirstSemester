# The variable password is set to the string "change me"
password = "changeme"
#counter is set to one 
AttemptCounter= 1

UserInput=input("Please type your password\n")
#This loop is repeated until the UserInput is equal to the value of the passowrd variable
while UserInput != password:

        if AttemptCounter == 5:
            print("Access denied, please press enter to exit and contact security to reset your password")
    #When the input doesn't equal to the value of passoword an output is displayed.
    #The user can try again as the value of the variable of UserInput is changed.
        UserInput=input("Try again\n")
        #+1 is added to the value of the counter
        AttemptCounter = AttemptCounter+1

        #When there has been 5 tries then the Access is denied.
       
            

if UserInput == password:
        print("Accepted")
        print("number of attempts = " + str(AttemptCounter))  
