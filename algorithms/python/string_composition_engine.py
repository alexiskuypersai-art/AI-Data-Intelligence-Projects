"""
    Goal: Build a new (n+1) x n string by cross-combining slices of two n x n squared strings.
    Key Concepts: String splitting, Symmetric indexing, and Progressive slicing.
    Example:
        s1 = "abcd\nefgh\nijkl\nmnop"
        s2 = "qrst\nuvwx\nyz12\n3456"
        compose(s1, s2) -> "a3456\nefyz1\nijkuv\nmnopq"
"""
def compose(s1, s2):
    lines1 = s1.split('\n')
    lines2 = s2.split('\n')
    n = len(lines1)
    result = []
    
    for i in range(n):
        parts_s1 = lines1[i][:i + 1]
        parts_s2 = lines2[n - 1 - i][:n - i]
        sum_parts = parts_s1 + parts_s2
        result.append(sum_parts)
    return '\n'.join(result)
