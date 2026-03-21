"""
TITLE: Better than Average (Codewars - 8 kyu)
OBJECTIVE: Compare personal test score against the class average.
LOGIC: The average must include the user's own points in the calculation.
DATE: 2026-03-21
"""

def better_than_average(class_points, your_points):
    class_sum = sum (class_points) + your_points
    class_len = len(class_points) + 1 
    class_mean = class_sum / class_len
    if your_points > class_mean: 
        return True
    else: 
        return False


# --- TEST CASES ---
if __name__ == "__main__":
    # Example 1: Average is 13.33 / Your score is 18 -> True
    print(f"Test 1: {better_than_average([10, 12], 18)}") 
    
    # Example 2: Average is 85 / Your score is 75 -> False
    print(f"Test 2: {better_than_average([90, 90], 75)}")
