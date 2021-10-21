import re

class Text:
    """Text class with countChar, countWords and countSentence methods"""
    def __init__(self, filePath):
        self.filePath = filePath
        self.symbols = 0
        self.words = 0
        self.sentences = 0

    def countChar(self):
        """Function that counts amount of symbols in file"""
        try:
            file = open(self.filePath, 'r') 
            for line in file:
                self.symbols += len(line)
            file.close()
            return self.symbols
        except IOError:
            raise IOError("File is not found")

    def countWords(self):
        """Function that counts amount of words in file"""
        try:
            f = open(self.filePath, 'r')
            for line in f:
                self.words += len(line.split())
            f.close()
            return self.words
        except IOError:
            raise IOError("File is not found")

    def countSentence(self):
        """Function that counts amount of sentences in file"""
        try:
            f = open(self.filePath, 'r')
            data = f.read()
            self.sentences = len(re.split('\. |! |\? |\... ', data))
            f.close()
            return self.sentences
        except IOError:
            raise IOError("File is not found")

x = Text("text.txt")
print("Words: " + str(x.countWords()))
print("Symbols: " + str(x.countChar()))
print("Sentences: " + str(x.countSentence()))
