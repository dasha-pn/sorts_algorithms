# Algorithms in Python

This repository contains implementations of several classical algorithms written in **Python**.  
The project includes multiple **sorting algorithms** as well as **Euclid’s algorithm** for computing the greatest common divisor (GCD).

The goal of this repository is to demonstrate basic algorithmic techniques and provide simple educational implementations with doctests.

---

# Implemented Algorithms

## Sorting Algorithms

### Bubble Sort

Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

**Time complexity**

- Worst case: $O(n^2)$  
- Average case: $O(n^2)$  
- Best case: $O(n)$

Example:

```python
from bubble_sort import bubble_sort

bubble_sort([9,8,7,6,5,4,3,2,1])
```

Output:
```
[1,2,3,4,5,6,7,8,9]
```
