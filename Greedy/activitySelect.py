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
    activities1 = [(1, 3), (2, 4), (3, 5)] # Small input
    activities2 = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)] # Medium input
    activities3 = [] # Edge case: No activities

    choice = input("Enter 1 for activities1, 2 for activities2, 3 for activities3: ")
    if choice == '1':
        result, selectedActivities = activitySelection(activities1)
    elif choice == '2':
        result, selectedActivities = activitySelection(activities2)
    elif choice == '3':
        result, selectedActivities = activitySelection(activities3)
   
    print("Selected activities:", selectedActivities)
    print("Count:", result)

    experimental_evaluation()

if __name__ == "__main__":
    main()
    
