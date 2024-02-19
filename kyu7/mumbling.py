"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
    accum("abcd") -> "A-Bb-Ccc-Dddd"
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(st):
    value = ""
    for i in range(0,len(st)):
        value += f"{st[i].upper()}{st[i].lower() * i}-"

    return value.rstrip("-")


print(accum("RqaEzty"))