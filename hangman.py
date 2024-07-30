class HangmanDictionary():
    def getWord(self):
        return 'Hangman'.lower()

class Hangman():
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.word = ''
        self.discoverWord = ''
        self.changes = 0
        
    def startGame(self):
        self.word = self.dictionary.getWord()
        self.discoverWord = list('_' * len(self.word))
        self.changes = 6

    def giveLetter(self, letter):
        result = False
        x = 0
        for char in self.word:
            if char == letter:
                self.discoverWord[x] = char
                result = True

            x += 1

        if not result:
            self.changes -= 1
        
        return result

    def getActualWord(self):
        return ''.join(self.discoverWord)

    def canPlay(self):
        return not self.win() and self.changes > 0

    def win(self):
        return self.getActualWord() == self.word

class Player():
    def __init__(self, letters):
        self.letters = list(letters)
        self.letters.reverse()
    
    def giveLetter(self):
        return self.letters.pop()

def game(player):
    hangman = Hangman(HangmanDictionary())
    hangman.startGame()
    
    while hangman.canPlay():
        hangman.giveLetter(player.giveLetter())

    return hangman.win()

print(game(Player('asdfghjklqwertyuiopzxcvbnm')))
