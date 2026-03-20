"""
TITLE: Word Value Calculator (Codewars)
OBJECTIVE: Calculate the score of words based on their alphabetical position and list index.
CONCEPTS: Enumerate (1-based), String iteration, ASCII conversion (ord), List comprehension logic.
"""

def name_value(my_list): 
    result = []
    for position, mot in enumerate(my_list, start=1):
        score = 0
        for letter in mot:
            if letter != ' ':
                # 'a' is 97 in ASCII, so ord(letter) - 96 gives a=1, b=2, etc.
                valeur = ord(letter) - 96
                score += valeur
        result.append(score * position)
    return result

# Example: name_value(["abc", "abc"]) -> [6, 12]
