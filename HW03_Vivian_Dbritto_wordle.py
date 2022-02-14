
def validate_word(EXPECTED_WORD, input_word):
    letter_counts: dict = {}
    appraisal = []

    # sort word in dictionary by letters
    for letter in EXPECTED_WORD:
        if letter in letter_counts.keys():
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    # validate if letter is present or missing
    for index in range(len(EXPECTED_WORD)):
        if input_word[index] == EXPECTED_WORD[index]:
            appraisal.append(' ')
            letter_counts[EXPECTED_WORD[index]] -= 1
        else:
            appraisal.append('"')

    # check if existing letter is placed in wrong position
    for index in range(len(EXPECTED_WORD)):
        if input_word[index] != EXPECTED_WORD[index]:
            if input_word[index] in letter_counts:
                if letter_counts[input_word[index]] > 0:
                    letter_counts[input_word[index]] -= 1
                    appraisal[index] = "'"

    print(''.join(appraisal))
