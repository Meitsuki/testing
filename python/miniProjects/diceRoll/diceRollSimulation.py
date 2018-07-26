import dice

print("Welcome to the dice roll simulator program!")
validPrompt = False

numDice = input("To get started, how many dice would you like to roll? ")
print("Excellent, you wish to roll " + str(numDice) + " dice.")
validPrompt = False
while not validPrompt:
    sameNumSides = input("Would you like these dice to all have the same number of sides? ")
    if sameNumSides.lower() == "yes" or sameNumSides.lower() == "no":
        validPrompt = True
    else:
        print("You have provided an invalid answer. Please enter Yes or No.")

print("Have a nice day.")
