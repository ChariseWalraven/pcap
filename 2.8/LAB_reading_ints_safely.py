# Your task is to write a function able to input integer values and to check if they are within a specified range.

# The function should:

# - accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
# - if the user enters a string that is not an integer value, the function should emit the
#   message Error: wrong input, and ask the user to input the value again;
# - if the user enters a number which falls outside the specified range, the function should
#   emit the message Error: the value is not within permitted range (min..max) and ask the
#   user to input the value again;
# - if the input value is valid, return it as a result.

def read_int(prompt, min, max):
    try:
        number = int(input(prompt))
        assert number > min and number < max
        return number
    except AssertionError:
        message = f"Error: the value is not within the permitted range ({min}..{max})"
        raise Exception(message)
    except ValueError:
        raise ValueError('Error: wrong input')


if __name__ == '__main__':
    valid = False
    n = None
    while not valid:
        try:
            n = read_int("Enter a number from -10 to 10: ", -10, 10)
            valid = True
        except KeyboardInterrupt:
            print('\nProgram stopped')
            break
        except BaseException as e:
            print(e)

        if n is not None:
            print("The number is:", n)


# Test data and expected output
# Enter a number from -10 to 10: 100
# Error: the value is not within permitted range (-10..10)
# Enter a number from -10 to 10: asd
# Error: wrong input
# Enter number from -10 to 10: 1
# The number is: 1
