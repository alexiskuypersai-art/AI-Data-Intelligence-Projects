"""
Name: Always Perfect
Challenge: Codewars (7 kyu)
Objective: (n * (n+1) * (n+2) * (n+3)) + 1 = Perfect Square
Concepts: String Parsing, Guard Clauses, Type Casting, Arithmetic.
Example: "1,2,3,4" -> "25, 5"
"""

def check_root(string_input):
    # 1. Split input into a list by commas
    elements = string_input.split(',')
    
    # 2. Ensure exactly 4 numbers are provided
    if len(elements) != 4:
        return "incorrect input"
        
    # 3. Convert strings to integers and catch non-numeric errors
    try:
        vals = [int(x) for x in elements]
    except ValueError:
        return "incorrect input"
        
    # 4. Validate if numbers are strictly consecutive
    is_consecutive = (vals[1] == vals[0] + 1 and 
                      vals[2] == vals[1] + 1 and 
                      vals[3] == vals[2] + 1)
                      
    if not is_consecutive:
        return "not consecutive"
        
    # 5. Calculate the product plus one
    total = (vals[0] * vals[1] * vals[2] * vals[3]) + 1
    
    # 6. Extract integer square root
    root = int(total ** 0.5)
    
    return f"{total}, {root}"

if __name__ == "__main__":
    # Quick verification
    print(check_root("1,2,3,4"))      # 25, 5
    print(check_root("10,11,12,13")) # 17161, 131
