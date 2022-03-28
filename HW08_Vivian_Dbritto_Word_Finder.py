from HW08_Vivian_Dbritto_Linked_List import LinkedList


def split(word):
    return list(word)


def getWordRank(word):
    print(word)
    file1 = open('wordRank.csv', 'r')
    lines = file1.readlines()
    for line in lines:
        list = line.split(",")
        if(list[1] == word):
            return list[0]
    return


def getPossibleWords():
    goodLetter = input(
        "Enter the good letters without space : ")
    badLetter = input(
        "Enter the bad letters without space : ")

    if(goodLetter or badLetter):
        letter1 = input("Enter the letter at position 1 : ")
        letter2 = input("Enter the letter at position 2 : ")
        letter3 = input("Enter the letter at position 3 : ")
        letter4 = input("Enter the letter at position 4 : ")
        letter5 = input("Enter the letter at position 5 : ")

        goodLetter_list = split(goodLetter)
        badLetter_list = split(badLetter)
        print(goodLetter_list)

        valid_words_file = open('wordList.txt', 'r')
        words = valid_words_file.readlines()
        l1 = LinkedList()
        l2 = LinkedList()
        word_dict = {}
        for word in words:
            word = word.strip()
            has_all_goodLetters = all(
                [char in word for char in goodLetter_list])
            has_no_badLetters = any([char in word for char in badLetter_list])

            if has_all_goodLetters == True and has_no_badLetters == False:
                l2.insert(word)
                if(letter1):
                    if(word[0] != letter1.strip()):
                        continue
                if(letter2):
                    if(word[1] != letter2.strip()):
                        continue
                if(letter3):
                    if(word[2] != letter3.strip()):
                        continue
                if(letter4):
                    if(word[3] != letter4.strip()):
                        continue
                if(letter5):
                    if(word[4] != letter5.strip()):
                        continue
                l1.insert(word)

        if l1.head:
            current = l1.head
        else:
            current = l2.head

        while(current):
            word_dict[current.data] = int(getWordRank(current.data.strip()))
            current = current.next
        sorted_list = dict(
            sorted(word_dict.items(), key=lambda x: x[1], reverse=True))
        return sorted_list.keys()
    else:
        file1 = open('wordRank.csv', 'r')
        lines = file1.readlines()
        result = []
        for line in lines:
            list = line.split(",")
            result.append(list[1])
        return result[0:50]


def main():
    x = getPossibleWords()
    if(len(x) > 0):
        print(*x, sep="\n")
    else:
        print('No combination found')


if __name__ == '__main__':
    main()
