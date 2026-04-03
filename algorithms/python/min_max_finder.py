def min_max(lst):
    """
    Goal:
        Identify the lowest and highest numbers within a given list  to simulate a "buy low, sell high" trading strategy.
    Key Concepts:
        - Built-in Functions: Utilizing min() and max() to efficiently 
          traverse an iterable structure (the list).
        - List Construction: Returning a new list [min, max] based 
          on the extracted extremes.
    Example:
        >>> min_max([1, 2, 3, 4, 5])
        [1, 5]
        >>> min_max([2334454, 5])
        [5, 2334454]
        >>> min_max([42])
        [42, 42]
    """
    buy_price = min(lst)
    sell_price = max(lst)
    return [buy_price, sell_price]
