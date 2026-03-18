"""
TITLE: Implementation of Nested Loops for String Scoring
GOAL: Calculate string values (a=1) and multiply by list index using enumerate.

Example:
Input: ["abc", "abc abc"] -> Output: [6, 24]
"""

def name_value(my_list): 
    result = []
    for position, mot in enumerate(my_list, start=1):
        score = 0
        for letter in mot:
            if letter != ' ':
                valeur = ord(letter) - 96
                score += valeur
        result.append(score * position)
    return result
