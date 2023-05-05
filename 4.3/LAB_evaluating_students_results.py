# Scenario

# Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements: the student's first name, the student's last name, and the number of point the student received during certain classes.

# The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

# The file may look as follows:

# John	Smith	5
# Anna	Boleyn	4.5
# John	Smith	2
# Anna	Boleyn	11
# Andrew	Cox	1.5

# Your task is to write a program which:

# asks the user for Prof. Jekyll's file name;
# reads the file contents and counts the sum of the received points for each student;
# prints a simple (but sorted) report, just like this one:
# Andrew Cox    1.5
# Anna Boleyn  15.5
# John Smith    7.0

# Note:

# your program must be fully protected against all possible failures: the file's non-existence, the file's emptiness, or any input data failures; encountering any data error should cause immediate program termination, and the erroneous should be presented to the user;
# implement and use your own exceptions hierarchy - we've presented it in the editor; the second exception should be raised when a bad line is detect, and the third when the source file exists but is empty.

# Tip: Use a dictionary to store the students' data.

# exceptions
class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass


def get_file_name():
    return input('Please enter the file name: ')


def read_file_contents(filename):
    f = open(filename, 'r')
    contents = f.read()
    if len(contents) == 0:
        raise FileEmpty()
    return contents

def sort_file_contents(file_contents):
    students = {}
    try:
        for line in file_contents.split('\n'):
            s_line = line.split(' ')
            name = ' '.join(s_line[0:2])
            score = s_line[-1]
            if name in students:
                students[name] += float(score)
            else:
                students[name] = float(score)
    except ValueError:
        raise BadLine()

    print(students)

if __name__ == '__main__':
    try:
        filename = get_file_name()
        file_contents = read_file_contents(filename)
        sort_file_contents(file_contents)
    except FileEmpty:
        print('The file specified is empty! Please select a file that is not empty.')
    except BadLine:
        print("There's something wrong with the data. Please check that all lines contain only student names and their scores.")
