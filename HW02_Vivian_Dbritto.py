# Pseudocode

# Initialize variables word_count = 6, word = "SONAR" and a empty list
# while word_count greater than 0
# take input from terminal and store in check_word
# if length of input word not equal to length of given word, print warning and ask user to input new word
# if input is not a word consisting of only alphabets, print warning and ask user to input new word
# convert input word to uppercase to validate
# if input is already entered in before trys, print warning and ask user to input new word
# if input word is equal to given word, print success message and exit the program
# Loop through the length of the input word and check each character of given word and input word, print the character and its
# position if characters match at a particular position
# add the input word to list
# decrement the try count

# No of trys
word_count = 6
# hidden word for game
word = "SONAR"
# list to store valid entered words
word_list = []

# loop till trys are exhausted
while (word_count > 0):
    # input from user
    check_word = input(f'\nEnter word of length {len(word)} to check\n')

    # check length of inputted and hidden word
    if (len(check_word) != len(word)):
        print(f'Please enter a word of length {len(word)}')
        continue

    # check word has only letters
    if not check_word.isalpha():
        print("Please enter word with only alphabets")
        continue

    # convert word to uppercase
    check_word = check_word.upper()

    # check word already inputted
    if check_word in word_list:
        print("Entered word already checked. Please try another word.")
        continue

    # compare input word with given word
    if check_word == word:
        print("\nWord match found !!!")
        exit()

    # check if character at particular index matches for input word and hidden word.
    for i in range(len(word)):
        if word[i] == check_word[i]:
            print(
                f'Character {check_word[i]} is present at position {i + 1}\n')
        else:
            print(
                f'Character {check_word[i]} is not present at position {i + 1}\n')

    # add input word to list
    word_list.append(check_word)
    # decrement try count
    word_count -= 1

print("You have exhausted all your trys. Please play again.")
