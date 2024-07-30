import math

class BenfordLaw():
    def __init__(self, numberSystemBase = 10):
        self.NumberSystemBase = numberSystemBase
        self._prepearTable()

    def analizeNumber(self, line):
        number = self._stringToNumber(line)
        firstDigit = self._getFirstDigit(number)

        if firstDigit != 0:
            self.table[firstDigit] += 1

    def printResults(self):
        print('Benford\'s Law:')

        for i in range(1, self.NumberSystemBase):
            print(str(i) + ') =', self.table[i])

    def _prepearTable(self):
        self.table = {}
        for i in  range(1, self.NumberSystemBase):
            self.table[i] = 0

        return self.table

    def _stringToNumber(self, line):
        return int(float(line))

    def _getFirstDigit(self, number):
        if number == 0:
            return 0

        multiplayer = math.floor(math.log(number, self.NumberSystemBase))
        numberBase = self.NumberSystemBase ** multiplayer
        firstDigit = math.floor(number / numberBase)

        return firstDigit

if __name__ == 'main':
    distribution = BenfordLaw()
    file = open('input.txt', 'r')

    for line in file:
        distribution.analizeNumber(line)

    distribution.printResults()
