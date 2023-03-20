def is_palindrome(text: str) -> str:
    try:
        text = text.replace(' ', '').lower()
        return text == text[::-1]
    except Exception as e:
        print('Whoops, something went wrong.', e)


def program():
    print('=' * 12, 'Palindrome Checker', '=' * 12)
    text = input('Enter some text to see if it\'s a palindrome: ')
    if is_palindrome(text):
        print('It\'s a palindrome')
    else:
        print('It\'s not a palindrome')


if __name__ == '__main__':
    program()

# test strings
# kayak
# loyal
# wow
# Ten animals I slam in a net
# 123214123123
