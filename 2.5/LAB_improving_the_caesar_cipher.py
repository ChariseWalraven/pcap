def caesar(text: str, shift_value: int) -> str:
    scrambled_text = ''
    for c in text:
        if c.isalpha():
            code = ord(c) + shift_value
            # check if the ascii decimal code of the character is past bounds
            if c.islower() and code > ord('z'):
                new_shift_value = code - ord('z') - 1  # -1 for 'a'
                code = ord('a') + new_shift_value
            elif c.isupper() and code > ord('Z'):
                new_shift_value = code - ord('Z') - 1
                code = ord('A') + new_shift_value
            scrambled_text += chr(code)
        else:
            scrambled_text += c

    return scrambled_text


def program():
    text = input('enter some text:')
    shift_value = input('enter a shift value:')

    try:
        shift_value = int(shift_value)
        scrambled_text = caesar(text, shift_value)
        print(scrambled_text)
    except Exception as e:
        print('An exception occurred.', e)


# TESTS
print(caesar('abcxyzABCxyz 123', 2) == 'cdezabCDEzab 123')
# cdezabCDEzab 123
print(caesar('The die is cast', 25) == 'Sgd chd hr bzrs')
# Sgd chd hr bzrs

# program()  # uncomment to run program
