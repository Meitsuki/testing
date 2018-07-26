import random

class dice:
    def __init__(self, numSides):
        self.numSides = numSides

    def rollDice(self):
        return random.randint(1,numSides)


class diceContainer:
    def __init__(self, numDice, sameNumSides = True, numSideForDice):
        self.numDice = numDice
        self.sameNumSides = sameNumSides
        self.numSideForDice = numSideForDice

        if sameNumSides:
            for x in range(numDice):
                diceContainer.append(dice(numSideForDice[0]))
        else:
            for x in range(numDice):
                diceContainer.append(dice(numSideForDice[x]))
