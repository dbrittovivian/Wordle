import HW03_Vivian_Dbritto_ui as ui
from HW03_Vivian_Dbritto_dictionary import Dictionary as dictionary
from HW03_Vivian_Dbritto_letterfrequency import frequency as frequency


class Wordle:

    gamesPlayed = 0
    gamesWon = 0
    guessDistribution = []

    def __init__(self):
        self.ui = ui.Ui()
        self.dictionary = dictionary()
        self.gamesPlayed = 0
        self.gamesWon = 0
        self.guessDistribution = [0, 0, 0, 0, 0, 0]

    def __str__(self) -> str:
        return f"Wordle(gamesPlayed:{str(self.gamesPlayed)}, gamesWon:{str(self.gamesWon)}, guessDistribution:{str(self.guessDistribution)})"

    def compareWord(self, a, b):
        if(a == b):
            return True
        else:
            return False

    def main(self):
        while(True):
            lltest = frequency()
            lltest.letterLikelyhood()
            f = open("gameplay.log", "a+")
            self.gamesPlayed = self.gamesPlayed + 1
            try:
                answer = self.dictionary.randomWord()
            except:
                print("Answer not found")
            try:
                self.dictionary.removeWord(answer)
            except:
                print("Remove word not working")
            f.write(f"Selected Word: {answer}\n")
            attempts = 1
            while(attempts < 7):
                word = self.ui.userinput(attempts)
                status = []
                while(self.dictionary.checkWord(word) != True):
                    print("Not a valid dictionary word")
                    word = self.ui.userinput(attempts)
                f.write(f"User Input:{word}\n")
                letter_counts: dict = {}  # making a dictionary to store the number of letters

                if(self.compareWord(word, answer)):
                    print("Correct Word! \n")
                    self.gamesWon = self.gamesWon + 1
                    self.guessDistribution[attempts-1] += 1
                    print(
                        "Now the word has been changed, to exit please press ENTER/RETURN")
                    break
                else:
                    for letter in answer:  # loop used to store the number of letters in the answer
                        if letter in letter_counts.keys():
                            letter_counts[letter] += 1
                        else:
                            letter_counts[letter] = 1
                    for index in range(len(answer)):  # loop used to store the status
                        if word[index] == answer[index]:
                            status.append(' ')
                            letter_counts[answer[index]] -= 1
                        else:
                            status.append('"')

                    for index in range(len(answer)):
                        if word[index] != answer[index]:
                            if word[index] in letter_counts:
                                if letter_counts[word[index]] > 0:
                                    letter_counts[word[index]] -= 1
                                    status[index] = "`"
                    attempts = attempts + 1
                    # printing the status after an attempt
                    print(''.join(status))
                if(attempts == 7):  # checking if this is the last attempt or not
                    print(f"The correct answer is #{answer}")
                    print(
                        "Now the word has been changed, to exit please press ENTER/RETURN")
            print("GAME STATISTICS")
            print(f"Total number of games played: {self.gamesPlayed}")
            print(
                f"Win percentage: {(self.gamesWon*100/self.gamesPlayed): .2f}%")
            print("Guess Distribution")
            print(f"Guessed in 1st attempt : {self.guessDistribution[0]}")
            print(f"Guessed in 2nd attempt : {self.guessDistribution[1]}")
            print(f"Guessed in 3rd attempt : {self.guessDistribution[2]}")
            print(f"Guessed in 4th attempt : {self.guessDistribution[3]}")
            print(f"Guessed in 5th attempt : {self.guessDistribution[4]}")
            print(f"Guessed in 6th attempt : {self.guessDistribution[5]}")
            f.write("User Report\n")
            f.write(f"Total number of games played: {self.gamesPlayed}\n")
            f.write(
                f"Win percentage: {(self.gamesWon*100/self.gamesPlayed): .2f}%\n")
            f.write(f"Guessed in 1st attempt : {self.guessDistribution[0]}\n")
            f.write(f"Guessed in 2nd attempt : {self.guessDistribution[1]}\n")
            f.write(f"Guessed in 3rd attempt : {self.guessDistribution[2]}\n")
            f.write(f"Guessed in 4th attempt : {self.guessDistribution[3]}\n")
            f.write(f"Guessed in 5th attempt : {self.guessDistribution[4]}\n")
            f.write(f"Guessed in 6th attempt : {self.guessDistribution[5]}\n")


if __name__ == "__main__":
    wordle = Wordle()
    wordle.main()
