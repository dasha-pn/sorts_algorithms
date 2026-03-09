"Quick sort"

def _partition(a: list, low: int, high: int) -> int:
    """Lomuto partition: використовуємо останній елемент як pivot."""

    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]
    return i + 1


def _quick_sort(a: list, low: int, high: int) -> None:
    if low < high:
        p = _partition(a, low, high)
        _quick_sort(a, low, p - 1)
        _quick_sort(a, p + 1, high)


def quick_sort(a: list) -> list:
    """
    Quick sort

    >>> quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    if len(a) <= 1:
        return a[:]
    arr = a[:]
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
