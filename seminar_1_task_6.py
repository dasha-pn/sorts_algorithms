"""Exercise 6"""

from typing import List, Tuple
import math

def closest_pair(nums: List[float]) -> Tuple[float, float, float]:
    """
    Повертає один оптимальний розв'язок: (x, y, |x-y|),
    де |x-y| — мінімальна різниця серед усіх пар.
    Час: O(n log n) за рахунок сортування. Пам'ять: O(n) через копію sorted().
    """

    n = len(nums)

    if n < 2:
        raise ValueError("Потрібно принаймні 2 елементи")

    a = sorted(nums)  # не мутуємо вхід
    best_diff = math.inf
    best_pair = (a[0], a[1])

    for i in range(1, n):
        d = abs(a[i] - a[i-1])
        if d < best_diff:
            best_diff = d
            best_pair = (a[i-1], a[i])

    return best_pair[0], best_pair[1], best_diff

def closest_pairs_all(nums: List[float]):
    """
    Повертає ВСІ пари з мінімальною різницею (список кортежів (x, y)).
    Корисно, якщо кілька сусідніх пар мають однакову мінімальну різницю.
    Час: O(n log n). Пам'ять: O(n).
    """

    n = len(nums)

    if n < 2:
        return []

    a = sorted(nums)
    diffs = [abs(a[i] - a[i-1]) for i in range(1, n)]
    min_diff = min(diffs)
    res = []

    for i in range(1, n):
        if abs(a[i] - a[i-1]) == min_diff:
            res.append((a[i-1], a[i]))

    return res, min_diff

if __name__ == "__main__":
    arr = [3.2, -1.0, 7.5, 3.1, 3.1000001, 9.0, 3.1002]
    print(closest_pair(arr))       # (3.1, 3.1000001, ~9.999999999621423e-08)
    print(closest_pairs_all(arr))  # ([(3.1, 3.1000001)], ~9.999999999621423e-08)
