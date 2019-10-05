# Linear search
# In linear search we have to loop through all
# element of the array till we get to matching
# target

# Basic binary search
# O(n) because the operational time is
# proportional to the input size n
import math


def linear_search(arr, target):
    for num in range(len(arr)):
        if arr[num] == target:
            return 1

    return -1


numbers = list(range(0, 50, 3))
# print(linear_search(numbers, 30))

# Note precedence of operators count
# in expression evaluation

# O(logn) => Logarithmic Time


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = int(math.floor((low + high) / 2))
        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return middle

    return -1


print(binary_search([20, 30, 40, 50, 60], 50))
