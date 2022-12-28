# keep in mind: this algorithm is used for education, not for real world problems
# -> More efficient algorithms are for example: quicksort, merge sort, timsort

elements = [20, 12, 15, 9, 4, 1, 18, 8, 13]


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                # instead of using "temp"
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print(elements)
bubble_sort(elements)
print("After using bubble sort:")
print(elements)
