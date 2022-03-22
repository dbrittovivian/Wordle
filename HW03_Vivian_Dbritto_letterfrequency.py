import string


class frequency:
    occurence = {}

    def __init__(self):
        [self.occurence.setdefault(x, [0, 0, 0, 0, 0])
         for x in string.ascii_uppercase]

    def __str__(self) -> str:
        return f"ll(occurence:{str(self.occurence)})"

    def letterLikelyhood(self):
        """Function to calculate the likelyhood of the letters"""
        f = open("wordList.txt", 'r')
        content = f.read()
        tempList = content.split('\n')
        f.close()
        for word in tempList:
            count = 0
            for letter in word:
                self.occurence[letter][count] += 1
                count += 1
        flag = 0
        for word in tempList:
            flag += 1
        for letter in string.ascii_uppercase:
            self.occurence[letter][0] = round(
                (self.occurence[letter][0] / flag), 3)
            self.occurence[letter][1] = round(
                (self.occurence[letter][1] / flag), 3)
            self.occurence[letter][2] = round(
                (self.occurence[letter][2] / flag), 3)
            self.occurence[letter][3] = round(
                (self.occurence[letter][3] / flag), 3)
            self.occurence[letter][4] = round(
                (self.occurence[letter][4] / flag), 3)
        f = open("letterFrequency.csv", 'w')
        f.write("letter,first_pos, second_pos, third_pos, fourth_pos, fifth_pos \n")
        for key in string.ascii_uppercase:
            f.write(
                f"{key}, {self.occurence[key][0]}, {self.occurence[key][1]}, {self.occurence[key][2]}, {self.occurence[key][3]}, {self.occurence[key][4]}\n")
        f.close()

    def dictListToTuple(self, dict):
        """Function to convert a list to tuple present in a dictionary"""
        for key in dict.keys():
            dict[key] = tuple(dict[key])

    def statToDict(self):
        """Function for reading data from a csv file and storing it into a dictionary"""
        f = open("letterFrequency.csv", 'r')
        content = f.read()
        tempList = content.split('\n')
        myDict = {}
        for line in range(1, len(tempList)):
            temp = tempList[line].split(", ")
            if self.checkTemp(temp):
                myDict[temp[0]] = (temp[1], temp[2], temp[3], temp[4], temp[5])
        return myDict

    def wordRank(self):
        """Function for calculating the ranks of the word present in the dictionary"""
        f = open("wordList.txt", 'r')
        content = f.read()
        tempList = content.split('\n')
        f.close()
        myDict = {}
        for word in tempList:
            likelyhood = float(self.occurence[word[0]][0]) * float(self.occurence[word[1]][1]) * float(
                self.occurence[word[2]][2]) * float(self.occurence[word[3]][3]) * float(self.occurence[word[4]][4])
            myDict[word] = likelyhood
        finalDict = sorted(myDict.items(), key=lambda x: x[1])
        finalDict.reverse()
        f = open("wordRank.csv", 'w')
        f.write("rank, word, likelyhood \n")
        flag = 1
        for word in finalDict:
            f.write(f"{flag}, {word[0]}, {word[1]}\n")
            flag += 1
        f.close()

    def checkTemp(self, temp):
        if(len(temp[0]) != 0):
            return True
        else:
            return False
