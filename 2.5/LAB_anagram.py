def is_anagram(text1: str, text2: str) -> bool:
    (text1, text2) = (text1.lower().replace(' ', ''), text2.lower().replace(' ', ''))
    if len(text1) <= 0 and len(text2) <= 0:
        return False
    elif len(text1) != len(text2):
        return False
    else:
        list_2 = [c for c in text2]
        for c in text1:
            idx = text2.find(c)
            if idx != -1:  # if character was found in both strings
                # remove character from text2 (ignore text1 since we're looping)
                del list_2[idx]
                text2 = ''.join(list_2)
            else:
                return False
        # if the list is empty after removing all the characters then both texts have the same type and number of
        # characters and are therefore anagrams.
        return len(list_2) == 0


def program():
    print('=' * 21, 'Are they Anagrams?', '=' * 21)
    print('A program that checks if two texts are anagrams of each other.')
    print('=' * 62, '\n')
    text1 = input('Enter the first text:')
    text2 = input('Enter the second text:')

    # Note: the instructions in the lab said to print 'Anagrams" if the inputs were anagrams and 'Not Anagrams' if they
    # weren't, but I thought that was boring so I changed it.
    if is_anagram(text1, text2):
        print('\nVerdict: Anagrams')
    else:
        print('\nVerdict: Not Anagrams')


# tests
# print(is_anagram('Listen', 'Silent'))
# print(is_anagram('norman', 'modern'))
# print(is_anagram('Tom Marvolo Riddle', 'I am Lord Voldemort'))

# program
if __name__ == "__main__":
    program()
