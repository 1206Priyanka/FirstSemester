#The richter value is set to what the user inputs and converted to a float.
richter = float(input("What is the magnitude of the eathquake?\n"))

#if richter value is 8 or higher then Most structures fall will be the output.
if richter >= 8 :
              print("Most structures fall")

#elif function is used to give different outputs for different richter value.
elif richter >=7:
              print("Many buildings destroyed")
              

elif richter >= 6:
              print("Many buildings considerably damaged some collapse")

elif richter >= 4.5 :
              print("Damage to poorly constructed buildings")

else:
              print("No destruction of buildings")
              
