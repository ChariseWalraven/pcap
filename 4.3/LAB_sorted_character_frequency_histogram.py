# Program that gets the histogram of the number of alphabetic characters and then outputs the sorted histogram to a file
from LAB_character_frequency_histogram import (
    get_file_content, get_filename, create_frequency_hist
)


def sort_hist(filename):
    hist = create_frequency_hist(get_file_content(filename))
    return dict(sorted(hist.items(), key=lambda item: item[1], reverse=True))


def output_to_hist_file(filename, hist):
    f = open(f'{filename}.hist', 'w+')
    for k, v in hist.items():
        s = f'{k} -> {v}\n'
        f.write(s)





if __name__ == "__main__":
    filename = get_filename()
    hist = sort_hist(filename)
    output_to_hist_file(filename, hist)

