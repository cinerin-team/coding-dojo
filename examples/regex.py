import re

if __name__ == '__main__':
    # Program to extract numbers from a string
    string = 'hello 12 hi 89. Howdy 34'
    pattern = r'\d+'

    result = re.findall(pattern, string)
    print(result)
    # Output: ['12', '89', '34']

    string = 'Twelve:12 Eighty nine:89.'
    pattern = r'\d+'

    result = re.split(pattern, string)
    print(result)

    # Output: ['Twelve:', ' Eighty nine:', '.']

    string = 'Twelve:12 Eighty nine:89 Nine:9.'
    pattern = r'\d+'

    # max split = 1
    # split only at the first occurrence
    result = re.split(pattern, string, 1)
    print(result)

    # Output: ['Twelve:', ' Eighty nine:89 Nine:9.']

    # Program to remove all whitespaces
    import re

    # multiline string
    string = 'abc 12 de 23 \n f45 6'

    # matches all whitespace characters
    pattern = r'\s+'

    # empty string
    replace = ''

    new_string = re.sub(pattern, replace, string)
    print(new_string)

    # Output: abc12de23f456

    string = "Python is fun"

    # check if 'Python' is at the beginning
    match = re.search(r'\APython', string)  # or "^Python"

    if match:
        print("pattern found inside the string")
    else:
        print("pattern not found")

        # Output: pattern found inside the string

    string = '39801 356, 2102 1111'

    # Three-digit number followed by space followed by two-digit number
    pattern = r'(\d{3}) (\d{2})'

    # match variable contains a Match object.
    match = re.search(pattern, string)

    if match:
        print(match.group())
    else:
        print("pattern not found")

    # Output: 801 35
    # >>> match.group(1)
    # '801'
    #
    # >>> match.group(2)
    # '35'
    # >>> match.group(1, 2)
    # ('801', '35')
    #
    # >>> match.groups()
    # ('801', '35')
