import random

class dice:
    def __init__(self, numSides):
        self.numSides = numSides

    def rollDice(self):
        return random.randint(1,self.numSides)


class diceContainer:
    def __init__(self, numDice, sameNumSides, numSideForDice):
        self.numDice = numDice
        self.sameNumSides = sameNumSides
        self.numSideForDice = numSideForDice

        if self.sameNumSides:
            for x in range(self.numDice):
                self.diceContainer.append(dice(numSideForDice[0]))
        else:
            for x in range(self.numDice):
                self.diceContainer.append(dice(numSideForDice[x]))

    def rollDiceContainer(self):
        for x in range(self.numDice):
            self.diceContainerRollResults.append(self.diceContainer[x].rollDice())
        return self.diceContainerRollResults
