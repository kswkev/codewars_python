"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
"""


def row_sum_odd_numbers(n):
    return sum([x for x in range(n**2 - (n-1), (n**2 - (n-1)) + ((n-1)*2) + 1, 2)])


print(f"1 = {row_sum_odd_numbers(1)}")
print(f"2 = {row_sum_odd_numbers(2)}")
print(f"3 = {row_sum_odd_numbers(3)}")
print(f"4 = {row_sum_odd_numbers(4)}")
print(f"5 = {row_sum_odd_numbers(5)}")
