# merge sort = divide and conquer algorithm
# O(n * log(n)) running time

def merge_sort(array):
    if len(array) > 1:
        # defining 2 sub arrays, with // i can get decimal division
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]
        # recursion
        merge_sort(left_array)
        merge_sort(right_array)
        # merge step
        i = 0 # left_array index
        j = 0 # right_array index
        k = 0 # merged array index
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1







elements = [20, 12, 15, 9, 4, 1, 18, 8, 13]
print(elements)
merge_sort(elements)
print(elements)
