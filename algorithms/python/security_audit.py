"""
    Goal: Count successful breaches where hacker_skill > security_level.
    Key Concepts: State mutation (security_level), Accumulator (count), Linear search.
    Example: ([7, 6, 8, 9], 6, 2) -> 1 breach (7 hits, 6 blocks so sec=8, 8 blocks so sec=10).
"""

def breach_attempts(hackers, security_level, increase):
    count_win = 0
    for i in hackers: 
        if i > security_level:
            count_win = count_win + 1 
        else:
            security_level = security_level + increase
    return compteur_win
