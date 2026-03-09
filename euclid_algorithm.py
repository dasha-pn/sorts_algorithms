"Euclid`s algorithm"

def euclid_algorithm(a: int, b: int) -> int:
    """
    Euclid`s algorithm
    
    >>> euclid_algorithm(2, 3)
    1
    """

    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
