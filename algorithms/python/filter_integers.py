""" 
INSTRUCTION: Filter a list of non-negative integers and strings, returning only integers..
CONCEPTS: 
  1. List Iteration (for i in l)
  2. Type Checking (isinstance)
  3. List Population (.append)
EXAMPLE: 
  filter_list([1, 2, 'a', 'b']) -> [1, 2]
  filter_list([1, 'a', 'b', 0, 15]) -> [1, 0, 15]
"""

def filter_list(l):
    new_list = []
    for i in l:
        if isinstance(i,int):
            new_list.append(i)
    return new_list
