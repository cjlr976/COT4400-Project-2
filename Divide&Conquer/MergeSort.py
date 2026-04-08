# Authors: Chloe Robinson, Camila Fienco, Tiffany Shi
# Purpose: Implementing Merge Sort using Divide and Conquer

# Function: Merge Sort
# Input: An array
# Output: A sorted array
from math import floor
import random
import time

def experimental_eval():
    '''
    Helper function to calculate the time it takes, in milliseconds, for the algorithm to
    complete with input sizes 10,100, and 1000. The values are randomly
    generated since this fuction is just testing the speed of the algorithm.
    '''
    print("--- Experimental Evaluation: ---\n")
    print("Input Size | Time")
    print("-------------------------")
    input_sizes = [10, 100, 1000]
    for size in input_sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        start_time = time.perf_counter()
        merge_sort(arr)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
        print(f"{size:<10} | {execution_time:.4f} ms")

def merge_sort(arr):
    #Base case
    if len(arr) <= 1:
        return arr

    #Divide recursively
    mid = floor(len(arr) / 2)
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    #Combine
    return merge(left_half, right_half)

#Conquer using merge function
def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

def main():
    #Test cases
    test_cases = [
        # Small input
        {"Name": "Small Array", "Array": [5, 2, 9, 1, 6]},
        
        # Medium input
        {"Name": "Medium Array", "Array": [42, 7, 91, 15, 63, 28, 84, 3, 56, 77, 
         19, 68, 24, 95, 11, 39, 72, 5, 88, 30]},

        # Edge cases
        {"Name": "Sorted Array", "Array": [1,2 ,8 ,10 ,18 ,20 ,23 ,34 ,45 ,59 ,102]}, #Already sorted array
        {"Name": "Reverse Sorted Array", "Array": [123 ,86 ,54 ,32 ,20 ,12 ,9]}, #Reverse sorted array
        {"Name": "Empty Array", "Array": []} #Empty array
    ]

    print("--- Merge Sort Test Cases ---\n")
    for test in test_cases:
        print(f"Test {test['Name']}")
        print(f"Array: {test['Array']}")

        # function call
        result = merge_sort(test["Array"])
        print(f"Sorted Array: {result}")
        print("-------------------------------\n")

    experimental_eval()


if __name__ == "__main__":
    main()