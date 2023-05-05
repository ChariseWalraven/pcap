# Program that counts the number of alphabetinc characters
def get_filename():
    return input('Please enter the filename: ')


def get_file_content(filename):
    f = open(filename, 'r')
    return f.read()


def create_frequency_hist(file_content):
    alpha = [c for c in file_content if c.isalpha()]

    hist = dict.fromkeys(alpha, 0)

    for c in alpha:
        hist[c] += 1

    return hist


if __name__ == "__main__":
    # filename = get_filename()
    file_content = get_file_content('test.txt')
    print(create_frequency_hist(file_content))


