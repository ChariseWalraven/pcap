"""Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

- it should accept exactly one argument - a string;
- it should return a list of words created from the string, divided in the places where the string contains whitespaces;
- if the string is empty, the function should return an empty list;
- its name should be mysplit()
"""


# TODO: Refactor for brevity and clarity
def mysplit(strng) -> list:
    results = []
    substring = ''
    for idx, c in enumerate(strng):
        substring += c
        substring = substring.strip()

        # if c is a whitespace character, or if this is the last character in strng, and substring is
        # not an empty string
        if (c.isspace() or idx == len(strng) - 1) and len(substring) > 0:
            results.append(substring)
            substring = ''

    return results


# Tests:
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(" a b c d e f "))
print(mysplit(""))

# Expected Output:
# ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
# ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
# []
# ['abc']
# []
