# bad running time, like bubblesort -> O(n²)
def insertion_sort(array):
    # beginning with index 1, because first element is "sorted"
    for i in range(1, len(array)):
        j =  i
        # check if the left neighbour is bigger than the current element
        while array[j -1] > array[j] and j > 0:
            # if yes, then swap
            array[j -1], array[j] = array[j], array[j -1]
            j -= 1





elements = [20, 12, 15, 9, 4, 1, 18, 8, 13]
print(elements)
insertion_sort(elements)
print(elements)
