"Merge sort"

def merge(array_1: list, array_2: list) -> list:
    "Merge part of the merge sirt algorithm"

    new_array = []

    while len(array_1) != 0 and len(array_2) != 0:
        if array_1[0] > array_2[0]:
            new_array.append(array_2[0])
            value_to_remove = array_2[0]
            array_2.remove(value_to_remove)
        else:
            new_array.append(array_1[0])
            value_to_remove = array_1[0]
            array_1.remove(value_to_remove)

    while len(array_1) != 0:
        new_array.append(array_1[0])
        value_to_remove = array_1[0]
        array_1.remove(value_to_remove)

    while len(array_2) != 0:
        new_array.append(array_2[0])
        value_to_remove = array_2[0]
        array_2.remove(value_to_remove)

    return new_array

def merge_sort(array: list) -> list:
    """
    Merge sort

    >>> merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    if len(array) == 1:
        return array

    mid = len(array)//2
    array_one = merge_sort(array[:mid])
    array_two = merge_sort(array[mid:])

    return merge(array_one, array_two)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
