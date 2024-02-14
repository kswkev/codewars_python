"""
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the
resulting string.

Note: input will never be an empty string
"""


def fake_bin(x):
    return ''.join([convert(item) for item in x])


def convert(item):
    if int(item) < 5:
        return "0"
    else:
        return "1"


print(fake_bin("45385593107843568"))
