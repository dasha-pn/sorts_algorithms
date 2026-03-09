"Bubble sort"

def bubble_sort(array: list) -> list:
    """
    Bubble sort

    >>> bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    for _ in range(1, len(array)):
        for j in range(0, len(array) - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    return array


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
