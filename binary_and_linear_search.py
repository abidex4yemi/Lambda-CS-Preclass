# Linear search
# In linear search we have to loop through all
# element of the array till we get to matching
# target

# Basic binary search


def linear_search(arr, target):
    for num in range(len(arr)):
        if arr[num] == target:
            return 1

    return -1


numbers = list(range(0, 50, 3))
print(linear_search(numbers, 30))
