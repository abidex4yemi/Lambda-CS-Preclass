# Insertion sort


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]

        j = i-1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = temp

    return arr


print(insertion_sort([200, 800, 20, 0, 10, 50]))
