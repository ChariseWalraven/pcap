"""Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

- it should accept exactly one argument - a string;
- it should return a list of words created from the string, divided in the places where the string contains whitespaces;
- if the string is empty, the function should return an empty list;
- its name should be mysplit()
"""


# TODO: Refactor for brevity and clarity
def mysplit(strng):
    lst = []
    substring = ''
    for c in strng:
        substring += c
        substring = substring.strip()

        if (c.isspace() or strng.rfind(c) == (len(strng) - 1)) and len(substring) > 0:
            lst.append(substring)
            substring = ''

    return lst


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

# Expected Output:
# ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
# ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
# []
# ['abc']
# []
