"""
    Goal: Find and return the professional role of an employee based on their full name.
    Key Concepts:
    - String Splitting: Uses .split() to separate the input string into first and last names.
    - Safety Handling: Uses a ternary operator to handle cases where only a first name is provided.
    - Dictionary Access: Iterates through a list of dictionaries, accessing data via keys (not indices).
    - Sequential Search: Returns the role immediately upon a match, or a default message if not found.
    Example:
    >>> find_employee_role("Dipper Pines")
    "Boss"
    >>> find_employee_role("Unknown Person")
    "Does not work here!"
    """
def find_employees_role(name):
    parts = name.split() 
    first = parts[0]
    last = parts[1] if len(parts) > 1 else ""

    for i in employees: 
        if i['first_name'] == first and i['last_name'] == last:
            return i['role']
    return "Does not work here!"
