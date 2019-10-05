# Selection sort


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = current_index

        for j in range(current_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        temp = arr[smallest_index]
        arr[smallest_index] = arr[current_index]
        arr[current_index] = temp

    return arr


print(selection_sort([20, 2, 90, 1, 0]))
