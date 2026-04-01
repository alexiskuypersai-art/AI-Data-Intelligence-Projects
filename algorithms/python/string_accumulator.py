"""
    Goal: 
        Transform a string by repeating each character based on its index, capitalized once then lowercased.
    Key Concepts: 
        enumerate(), string multiplication (*), .upper(), .lower(), .join().
    Example:
        >>> accum("abcd") = "A-Bb-Ccc-Dddd"
        >>> accum("RqaEzty") = "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
"""
def accum(st):
    result = []
    for index, letter in enumerate(st):
        parts = letter.upper() + (letter.lower() * index)
        result.append(parts)
    return "-".join(result)
