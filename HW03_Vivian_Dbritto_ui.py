import logging
import random
import HW03_Vivian_Dbritto_dictionary as dict
import HW03_Vivian_Dbritto_wordle as wordle


def start_game(word, game_count, won_count, logger):
    attempt = 0
    game_count += 1
    # No of trys
    word_count = 6
    # hidden word for game
    word = word.upper()
    # list to store valid entered words
    word_list = []
    logger.info(f'Current word: {word}')
    print(word)

    # loop till trys are exhausted
    i = 1
    while (i <= word_count):
        # input from user
        check_word = input(
            f'\nAttempt #{i}: Enter word of length {len(word)} to check\n')
        logger.info(f'Attempt #{i}: {check_word}')

        # check length of inputted and hidden word
        if (len(check_word) != len(word)):
            print(f'Please enter a word of length {len(word)}')
            logger.error(f'Please enter a word of length {len(word)}')
            continue

        # check word has only letters
        if not check_word.isalpha():
            print("Please enter word with only alphabets")
            logger.error("Please enter word with only alphabets")
            continue

        # convert word to uppercase
        check_word = check_word.upper()

        # check word already inputted
        if check_word in word_list:
            print("Entered word already checked. Please try another word.")
            logger.error(
                "Entered word already checked. Please try another word.")
            continue

        # compare input word with given word
        if check_word == word:
            print("\nWord match found !!!")
            logger.info("Word match found !!!")
            won_count += 1
            attempt = i
            break

        # check if character at particular index matches for input word and hidden word.
        print(wordle.validate_word(word, check_word))

        # add input word to list
        word_list.append(check_word)
        # decrement try count
        i += 1
    else:
        print("You have exhausted all your trys. Please play again.")
        attempt = 0

    print("\n******* Statistics *********\n")
    print(f"Played: {game_count}\n")
    print(f"Won%: {(won_count/game_count*100)}\n")
    print("\n******* Guess Distribution *********\n")
    print(f"Attempt 1: {1 if attempt == 1 else 0}\n")
    print(f"Attempt 2: {1 if attempt == 2 else 0}\n")
    print(f"Attempt 3: {1 if attempt == 3 else 0}\n")
    print(f"Attempt 4: {1 if attempt == 4 else 0}\n")
    print(f"Attempt 5: {1 if attempt == 5 else 0}\n")
    print(f"Attempt 6: {1 if attempt == 6 else 0}\n")

    logger.info("******* Statistics *********")
    logger.info(f"Played: {game_count}")
    logger.info(f"Won%: {(won_count/game_count*100)}")
    logger.info("******* Guess Distribution *********")
    logger.info(f"Attempt 1: {1 if attempt == 1 else 0}")
    logger.info(f"Attempt 2: {1 if attempt == 2 else 0}")
    logger.info(f"Attempt 3: {1 if attempt == 3 else 0}")
    logger.info(f"Attempt 4: {1 if attempt == 4 else 0}")
    logger.info(f"Attempt 5: {1 if attempt == 5 else 0}")
    logger.info(f"Attempt 6: {1 if attempt == 6 else 0}")

    return game_count, won_count


def main():
    game_count = 0
    won_count = 0
    logger = log()
    word_list = dict.get_all_5_letter_words()
    word = random.choice(word_list)
    word_list.remove(word)
    game_count, won_count = start_game(word, game_count, won_count, logger)
    # Game continues till empty string entered
    ans = input()
    while ans != "":
        if len(word_list == 0):
            word_list = dict.get_all_5_letter_words()

        word = random.choice(word_list)
        word_list.remove(word)
        game_count, won_count = start_game(word, game_count, won_count, logger)
        ans = input()
    else:
        exit()


def log():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    file_handler = logging.FileHandler('gameplay.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


if __name__ == "__main__":
    main()
