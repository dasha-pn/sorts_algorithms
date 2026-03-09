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

### Insertion Sort

Insertion sort builds the sorted array one element at a time by inserting each element into its correct position.

**Time complexity**

- Worst case: $O(n^2)$  
- Average case: $O(n^2)$  
- Best case: $O(n)$  

Example:

```python
from insertion_sort import insertion_sort

insertion_sort([9,8,7,6,5,4,3,2,1])
```

### Merge Sort

Merge sort is a **divide-and-conquer algorithm**.  
It recursively splits the array into halves, sorts them, and then merges them.

**Time complexity**

- Worst case: $O(n \log n)$  
- Average case: $O(n \log n)$  
- Best case: $O(n \log n)$  

Example:

```python
from merge_sort import merge_sort

merge_sort([9,8,7,6,5,4,3,2,1])
```

### Quick Sort

Quick sort is another **divide-and-conquer algorithm** that selects a pivot element and partitions the array around it.

**Time complexity**

- Worst case: $O(n^2)$  
- Average case: $O(n \log n)$  
- Best case: $O(n \log n)$  

Example:

```python
from quick_sort import quick_sort

quick_sort([9,8,7,6,5,4,3,2,1])
```

## Euclid’s Algorithm

Euclid’s algorithm is used to compute the **greatest common divisor (GCD)** of two integers.

The algorithm is based on the identity:

$$
gcd(a,b) = gcd(b, a \bmod b)
$$

Example:

```python
from euclid_algorithm import euclid_algorithm

euclid_algorithm(2,3)
```

Output:
```
1
```

### Purpose of the Project

This repository was created for educational purposes:

- practicing implementation of classical algorithms

- understanding algorithm complexity

- learning Python doctests

- comparing different sorting techniques
