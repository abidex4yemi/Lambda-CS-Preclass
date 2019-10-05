# Basic bubble sort
# O(n squared)


def bubble_sort(arr):
    array_length = len(arr)

    for i in range(array_length):
        for j in range(0, array_length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble_sort([20, 10, 4, 9, 1, 0, 43]))
