import HW03_Vivian_Dbritto_dictionary as dict
import HW03_Vivian_Dbritto_wordle as wordle


def start_game():
    # No of trys
    word_count = 6
    # hidden word for game
    word = dict.get_random_5_letter_word().upper()
    # list to store valid entered words
    word_list = []

    # loop till trys are exhausted
    i = 1
    while (i <= word_count):
        # input from user
        check_word = input(
            f'\nAttempt #{i}: Enter word of length {len(word)} to check\n')

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
            break

        # check if character at particular index matches for input word and hidden word.
        wordle.validate_word(word, check_word)

        # add input word to list
        word_list.append(check_word)
        # decrement try count
        i += 1
    else:
        print("You have exhausted all your trys. Please play again.")


def main():
    start_game()
    # Game continues till empty string entered
    ans = input()
    while ans != "":
        start_game()
        ans = input()
    else:
        exit()


if __name__ == "__main__":
    main()
