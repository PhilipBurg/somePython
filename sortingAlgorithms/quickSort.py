# like merge sort: divide and conquer algorithm
# running time: O(n²) worst case, O(n*log(n)) best and average case



def quick_sort(array):
    left = []
    right = []
    equal = []

    if len(array) > 1:
        pivot = array[-1] # set last elem as pivot
        for i in array:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            elif i == pivot:
                equal.append(i)
        return quick_sort(left) + equal + quick_sort(right)
    else:
        return array

elements = [20, 12, 15, 9, 4, 1, 18, 8, 13]
print(quick_sort(elements))