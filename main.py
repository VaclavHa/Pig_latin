CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


def main(word: str) -> str:
    """
    When words starts with consonant the consonant is moved to the end of the word and 'ay' is added.
    If it is a vowel then 'way' is just added to the end.
    """
    if not word:  # Check if the word is empty
        return 'Input is empty. Please enter a word.'
    if not word.isalpha():  # Check if word is of only letters
        return 'Input only letters. No special symbols or digits allowed.'

    if word[0].lower() in CONSONANTS:
        new_word = word[1:] + word[0] + 'ay'
        return new_word.lower()
    else:
        new_word = word + 'way'
        return new_word.lower()


if __name__ == '__main__':
    word = input("Choose a word to be translated: ")
    new_word = main(word)
    print(new_word)
