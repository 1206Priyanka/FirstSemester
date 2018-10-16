password = "changeme"
AttemptCounter= 0

UserInput=input("Please type your password")

while UserInput != password:
        UserInput=input("Try again")
        
        AttemptCounter = AttemptCounter+1

if UserInput == password:
        print("Accepted")
        print("number of attempts = " + AttemptCounter)    
