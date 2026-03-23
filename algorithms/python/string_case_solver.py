"""
    TITLE: Mixed Case String Converter
    
    Converts string to uniform case based on majority.
    Rules: Upper wins if count > lower; otherwise lower wins (handles equality).
    Concepts: String Iteration, Boolean Check (.isupper), Counter Pattern.
    Examples:
    solve("code") = "code"
    solve("CODe") = "CODE"
    solve("COde") = "code"
"""

def solve(s):
    upper_count = 0
    for char in s : 
        if char.isupper() :
            upper_count = upper_count + 1 
        else : 
            upper_count = upper_count - 1
    if upper_count > 0 : 
        return s.upper()
    else : 
        return s.lower()
