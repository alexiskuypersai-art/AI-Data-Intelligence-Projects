"""
TITLE: Nested Function Calls (The Santa Claus Logic)
OBJECTIVE: Understand how function returns are passed as arguments to the next call.
CONCEPTS: String concatenation, Nested function execution.
"""


def ho(wagon=None):
    if wagon is None:
        return "Ho!"
    return "Ho " + wagon

print(ho(ho(ho())))
# Expected Output: "Ho Ho Ho!"
