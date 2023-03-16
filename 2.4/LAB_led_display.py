S = '$'  # symbol to use. change this for a different look
line = S * 3
end = ' ' * 2 + S
start = S + ' ' * 2
middle = ' ' + S + ' '
edges = S + ' ' + S

number_dict = {
    '1': [
        end,
        end,
        end,
        end,
        end,
    ],
    '2': [
        line,
        end,
        line,
        start,
        line,
    ],
    '3': [
        line,
        end,
        line,
        end,
        line,
    ],
    '4': [
        edges,
        edges,
        line,
        end,
        end,
    ],
    '5': [
        line,
        start,
        line,
        end,
        line,
    ],
    '6': [
        line,
        start,
        line,
        edges,
        line,
    ],
    '7': [
        line,
        end,
        end,
        end,
        end,
    ],
    '8': [
        line,
        edges,
        line,
        edges,
        line,
    ],
    '9': [
        line,
        edges,
        line,
        end,
        line,
    ],
    '0': [
        line,
        edges,
        edges,
        edges,
        line,
    ],
}


def display_number(number: int) -> str:
    display = ''
    number_str = str(number)

    for row in range(5):
        for n in number_str:
            display += number_dict[n][row]
            display += ' '
        display += '\n'

    print(display)


# Tests:
display_number(123)
display_number(9081726354)
