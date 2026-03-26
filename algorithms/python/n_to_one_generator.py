"""
    Goal:
      Generates a sequence of integers starting from a given number 'n' 
      and moving step-by-step towards the number 1.
    Key Concepts:
    - Directional Logic: If n > 1, the sequence decreases. If n < 1, it increases.
    - While Loop: Continues execution until the current value reaches the target (1).
    - Edge Case Handling: Works for positive, negative, and large integers (-9999 to 9999).
    Example:
        >>> seq_to_one(5)
        [5, 4, 3, 2, 1]
        >>> seq_to_one(-2)
        [-2, -1, 0, 1]
        >>> seq_to_one(1)
        [1]
    """
def seq_to_one(n):
    result = []
    while n != 1 :
        result.append(n)
        if n > 1:
            n = n - 1 
        else : 
            n = n + 1 
    result.append(1)
    return result
