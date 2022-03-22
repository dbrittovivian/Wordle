class Ui:
    inputList = []

    def __init__(self):
        self.inputList = []

    def __str__(self) -> str:
        return f"InputList:{str(self.inputList)}"

    def quitfunction(self, a):
        if(len(a) == 0):
            return True
        else:
            return False

    def userinput(self, k):

        print(f"Attempt #{k}:")
        print("Any 5 letter word")
        word = input()
        word = word.upper()
        if(self.quitfunction(word)):
            quit()

        if len(word) != 5 or word in self.inputList or not word.isalpha():
            print("Input should be a unique 5 letter word")
            return "incorrect input"
        else:
            self.inputList.append(word)
            k = k+1
            return word
