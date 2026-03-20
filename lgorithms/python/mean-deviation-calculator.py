    """
    Calculates the difference between the mean of a list and each of its elements.
    Returns a list of differences rounded to 2 decimal places.
    """
   
    # 1. Calculate the mean
    def distances_from_average(test_list):
    total_sum = sum(test_list)
    count = len(test_list)
    mean = total_sum / count
    
    # 2. Initialize the result container
    result = []
    
    # 3. Iterate through the list to calculate deviations
    for i in test_list:
        # Difference = Mean - Current Value
        diff = round(mean - i, 2)
        result.append(diff)
    
    # 4. Return the completed list
    return result

# Usage
data = [55, 95, 62, 36, 48]
print(distances_from_average(data)) 
# Output: [4.2, -35.8, -2.8, 23.2, 11.2]
