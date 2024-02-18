"""
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.
Example:
h = 0
m = 1
s = 1

result = 61000
"""


def past(h, m, s):
    return (s * 1000) + (m * 60 * 1000) + (h * 60 * 60 * 1000)


print(past(0,1,1))
