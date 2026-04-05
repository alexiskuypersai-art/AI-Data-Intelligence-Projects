"""
Goal:
  Find the indices of two numbers in an integer array 'nums' that sum up to 
  a specific 'target'. Each input has exactly one solution.
Key Concepts:
  - Nested For-Loops: Iterating through a list with two pointers (i and j).
  - List Indexing: Accessing elements by their position using range(len()).
  - Arithmetic Logic: Checking the sum condition (nums[i] + nums[j] == target).
Example:
    Input: nums = [3, 2, 4], target = 6
    Logic: 
        i=0 (3) + j=1 (2) = 5 (No)
        i=1 (2) + j=2 (4) = 6 (Yes!)
    Output: [1, 2]
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
