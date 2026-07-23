def selectionSort(array, size):
    for ind in range(size - 1):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j

        array[ind], array[min_index] = array[min_index], array[ind]

arr = [5,2,6,1,3,4]
size = len(arr)
selectionSort(arr, size)

print(arr)
