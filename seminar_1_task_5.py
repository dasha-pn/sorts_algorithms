"""Seminar 1 task 5"""

def intersection_unique(a: list[int], b: list[int]) -> list[int]:
    """
    Повертає спільні елементи БЕЗ повторів (у зростаючому порядку).
    Обидва списки a і b мають бути вже відсортовані.
    """

    i = 0
    j = 0
    res = []
    last = None #щоб уникати дублювання у відповіді

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if last != a[i]:
                res.append(a[i])
                last = a[i]
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    return res

def intersection_multi(a: list[int], b: list[int]) -> list[int]:
    """
    Повертає спільні елементи З повторами (multiset-перетин), у зростаючому порядку.
    Обидва списки a і b мають бути вже відсортовані.
    """

    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            res.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return res

if __name__ == "__main__":
    A = [1, 2, 2, 3, 5, 7]
    B = [2, 2, 2, 3, 6, 7, 8]
    print(intersection_unique(A, B))  # [2, 3, 7]
    print(intersection_multi(A, B))   # [2, 2, 3, 7]
