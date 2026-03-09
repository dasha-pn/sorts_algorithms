"Insertion sort"

def insertion_sort(array: list) -> list:
    """
    Insertion sort

    >>> insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            temp = array[j-1]
            array[j-1] = array[j]
            array[j] = temp
            j = j - 1

    return array

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
