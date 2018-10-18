password = "changeme"
AttemptCounter= 1

UserInput=input("Please type your password\n")

while UserInput != password:
        UserInput=input("Try again\n")
        
        AttemptCounter = AttemptCounter+1
        if AttemptCounter == 5:
            print("Access denied, please press enter to exit and contact security to reset your password")
            

if UserInput == password:
        print("Accepted")
        print("number of attempts = " + str(AttemptCounter))  
