def calculate_digit_of_life(birth_date: str) -> int:
    digit_of_life = 0
    for c in birth_date:
        i = int(c)
        digit_of_life += i

    while len(str(digit_of_life)) > 1:
        digit_of_life = calculate_digit_of_life(str(digit_of_life))

    return digit_of_life


def program():
    print('=' * 21, 'Digit Of Life Calculator', '=' * 21, '\n')
    birth_date = input('Enter your birth date (YYYYMMDD/YYYYDDMM/MMDDYYYY - no separators): ')
    print(calculate_digit_of_life(birth_date))


# tests
# print(calculate_digit_of_life('19970217'))
# 9


if __name__ == '__main__':
    try:
        program()
    except (TypeError, ValueError):
        print('Whoops, there was an error with the data. Are you sure you entered the correct format?')
    except Exception as e:
        print('Whoops, something went wrong.', e)
