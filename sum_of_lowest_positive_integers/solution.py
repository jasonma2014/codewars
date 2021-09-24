"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""
import sys


def sum_two_smallest_numbers(numbers):
    first = second = sys.maxsize
    for i in range(len(numbers)):
        # if current number is below or equals zero, jump to next iterate
        if numbers[i] <= 0:
            continue
        # if current num is smaller than first then
        # update both first and second
        if numbers[i] < first:
            second = first
            first = numbers[i]

        # if current number is between first and second then
        # update the second
        if first < numbers[i] < second:
            second = numbers[i]

    total = first + second
    return total
