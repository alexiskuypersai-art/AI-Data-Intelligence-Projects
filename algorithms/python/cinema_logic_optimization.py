"""
    Title: Cinema Loyalty System Profitability Analysis
    Goal:
    To determine the minimum number of cinema sessions (n) required so that 
    the cumulative cost of System B (rounded up to the next dollar) 
    becomes strictly cheaper than the total cost of System A.    
    Concept : 
    - Accumulator Pattern: Building totals using the '+=' operator.
    - While Loop: Iterating based on a dynamic condition rather than a fixed range.
    - Geometric Sequence: Reducing the ticket price by a percentage each turn.
    - Type Casting: Using int() to simulate rounding logic. 
"""
def movie(card, ticket, perc):
    session = 0
    total_a = 0
    total_b = card
    ticket_b = ticket
    while not (total_a > int(total_b + 0.9999999999)):
        session = session + 1 
        total_a += ticket
        ticket_b = ticket_b * perc
        total_b += ticket_b
        
    return session
