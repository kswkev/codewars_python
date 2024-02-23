"""
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
"""


def stray(arr):
    first_attempt = [item for item in arr if item == arr[0]]
    if len(first_attempt) == 1:
        return first_attempt[0]
    else:
        second_attempt = [item for item in arr if item != first_attempt[0]]
        return second_attempt[0]


print(stray([1, 1, 1, 1, 1, 1, 2]))
