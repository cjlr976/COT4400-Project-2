# Authors: Chloe Robinson, Camila Fienco, Tiffany Shi
# Purpose: Implementing Activity Selection using Greedy Approach

# Function: Activity Selection Problem 
# Input: List of activities with their start and end times
# Output: Maximum number of activities that can be performed by a single person

import time 
import random 

# Function to perform experimental evaluation of the activity selection algorithm
def experimental_evaluation():
    print("\nInput Size  Time")

    input_sizes = [10, 100, 1000]

    for size in input_sizes:
        activities = []

        for _ in range(size):
            # Generates random start and finish times for activites
            start = random.randint(0, size * 10)
            end = random.randint(start + 1, start + 10)
            activities.append((start, end))

        start_time = time.perf_counter()
        activitySelection(activities)
        end_time = time.perf_counter()

        execution_time = (end_time - start_time) * 1000

        print(f"{size:<10}  {execution_time:.4f} ms")

def activitySelection(activities):
    # Adds index to each activity for tracking
    activities = [(start, end, i + 1) for i, (start, end) in enumerate(activities)] 
    # Sort activities based on their finish times
    activities.sort(key=lambda x: x[1]) 

    count = 0 
    last_end = float('-inf')
    selected = []

    # Iterate through sorted activities
    for start, end, index in activities: 
        if start >= last_end:
            count += 1
            last_end = end
            selected.append(index)
        
    # Return both the count of selected activities and their indices
    return count, selected 

def main():
    # Test cases
    test_cases = [
        {"Name":"Small input", "Activities": [(3, 5), (1, 3), (2, 4)]  }, # Small input
        {"Name":"Medium input", "Activities": [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]}, # Medium input
        {"Name":"Edge case", "Activities": []} # Edge case: No activities
    ]

    print("--- Select Activities Test Cases ---\n")
    for test in test_cases:
        print(f"Test:{test['Name']}")
        print(f"Test:{test['Activities']}")

        count, selected = activitySelection(test["Activities"])
        print(f"Maximum activities selected:{count}")
        print(f"Selected activity indices:{selected}")
        print("-------------------------------\n")


    experimental_evaluation()

if __name__ == "__main__":
    main()
    
