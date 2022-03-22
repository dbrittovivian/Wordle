import random
import os


class Dictionary:

    filteredList = []

    def __init__(self):
        f = open("words.txt", "r")
        content = f.read()
        wordList = content.split("\n")
        f.close()
        f = open("wordList.txt", "w")
        for word in wordList:
            if(len(word) == 5):
                f.write(f"{word.upper()}\n")
        f.close()
        f = open("wordList.txt", "r")
        content = f.read()
        self.filteredList = content.split('\n')
        f.close()

    def __str__(self) -> str:
        return f"Dictionary(filteredList:{str(self.filteredList)})"

    def randomWord(self):
        return random.choice(self.filteredList)

    def checkWord(self, word):
        if(word in self.filteredList):
            return True
        else:
            return False

    def removeWord(self, word):
        with open("wordList.txt", "r") as f:
            lines = f.readlines()
        with open("wordList.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != word:
                    f.write(line)
        if(self.fileSize()):
            try:
                self.resetWords()
            except:
                print("Reset words not working")

    def resetWords(self):
        f = open("wordList", "w")
        f.write(self.filteredList)
        f.close()

    def fileSize(self):
        if os.stat("wordList.txt").st_size == 0:
            return True
        else:
            return False
