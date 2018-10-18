password = "changeme"
AttemptCounter= 1

UserInput=input("Please type your password\n")

while UserInput != password:
        UserInput=input("Try again\n")
        
        AttemptCounter = AttemptCounter+1

if UserInput == password:
        print("Accepted")
        print("number of attempts = " + str(AttemptCounter))    
