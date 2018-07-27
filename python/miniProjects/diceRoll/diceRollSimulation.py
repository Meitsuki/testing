import dice

print("Welcome to the dice roll simulator program!")
validPrompt = False

while not validPrompt:
    numDice = input("To get started, how many dice would you like to roll? ")
    validInt = False
    try:
        numDice = int(numDice) + 0
        validInt = True
    except TypeError:
        validInt = False
    if validInt:
        if numDice >= 1:
            validPrompt = True
        else:
            print("Please provide a positive integer.")
    else:
        print("You have provided an invalid input, please enter a positive integer.")

print("Excellent, you wish to roll " + str(numDice) + " dice.")

validPrompt = False
sameNumSides = False
while not validPrompt:
    sameNumSides = input("Would you like these dice to all have the same number of sides? ")
    if sameNumSides.lower() == "yes" or sameNumSides.lower() == "no":
        validPrompt = True
    else:
        print("You have provided an invalid answer. Please enter Yes or No.")

if sameNumSides.lower() == "yes":
    sameNumSides = True
else:
    sameNumSides = False

validIntPrompt = False
if sameNumSides:
    numSides = input("How many sides do you wish the dice to have? )
else:
    for x in range(numDice):
        numSides = input("How many sides do you wish dice " + str(x) + " to have? ")
        sidesForDice.append(numSides)

dices = diceContainer(numDice, sameNumSides, sidesForDice)
print("Have a nice day.")
