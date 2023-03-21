def is_word_in_text(word: str, text: str) -> bool:
    text_list = [c for c in text]
    for c in word:
        if c in text_list:
            del text_list[text_list.index(c)]

    num_chars_found = len(text) - len(text_list)

    if num_chars_found != len(word):
        return False
    else:
        return True


def program():
    print('=' * 21, 'Find A Word', '=' * 21)
    print('Checks if the word given can be made using letters from the text given.', end='\n\n')
    word = input('Enter the word you want to find in the text: ')
    text = input('Now enter the text to check: ')
    print()

    if is_word_in_text(word, text):
        print('Yes')
    else:
        print('No')


# tests
# print(is_word_in_text('donor', 'Nabucodonosor'))
# True / Yes (if using program())
# print(is_word_in_text('donut', 'Nabucodonosor'))
# print(is_word_in_text('nauts', 'Badsoanuadts'))
# False / No (if using program())


if __name__ == '__main__':
    program()
