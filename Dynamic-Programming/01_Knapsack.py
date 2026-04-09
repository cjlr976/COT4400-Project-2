# Authors: Chloe Robinson, Camila Fienco, Tiffany Shi
# Purpose: Implementing 0/1 Knapsack using Dynamic Programming

# Function: 0/1 Knapsack
# Input: Weights array, values array, capacity of knapsack
# Output: Maximum value achievable 


import time
import random

def experimental_eval():
    '''
    Helper function to calculate the time it takes, in milliseconds, for the algorithm to
    complete with input sizes 10,100, and 1000. The values are randomly
    generated since this fuction is just testing the speed of the algorithm.
    '''

    print("--- Experimental Evaluation: ---\n")
    print("--- Experiment 1: Capacity Scales with Input ---\n")
    print("Input Size | Time")
    print("-------------------------")

    input_sizes = [10, 100, 1000]

    for size in input_sizes:
        # generate random weights and values for the current size
        weights = [random.randint(1, 100) for _ in range(size)]
        values = [random.randint(1, 100) for _ in range(size)]

        #scale capacity with the input size
        capacity = random.randint(size * 2, size * 5)

        start_time = time.perf_counter()
        knapsack(weights, values, capacity, False)
        end_time = time.perf_counter()

        # calculate milliseconds
        execution_time = (end_time - start_time) * 1000

        print(f"{size:<10} | {execution_time:.4f} ms")

    print("\n--- Experiment 2: Capacity Is Constant ---\n")
    print("Input Size | Time")
    print("-------------------------")

    input_sizes = [10, 100, 1000]

    for size in input_sizes:
        # generate random weights and values for the current size
        weights = [random.randint(1, 100) for _ in range(size)]
        values = [random.randint(1, 100) for _ in range(size)]

        #scale capacity with the input size
        capacity = 100

        start_time = time.perf_counter()
        knapsack(weights, values, capacity, False)
        end_time = time.perf_counter()

        # calculate milliseconds
        execution_time = (end_time - start_time) * 1000

        print(f"{size:<10} | {execution_time:.4f} ms")


def knapsack(weights, values, capacity, show_output = True):
    '''
    Performs the 0/1 Knapsack Algorithm
    '''

    num_items = len(weights)

    # cols are weight of knapsack, rows are available items
    matrix = [[0] * (capacity + 1) for _ in range(num_items + 1)]

    for item in range(1, num_items + 1):
        for cur_weight in range(1, capacity + 1):

            # check if item's weight fits in current capacity
            if weights[item - 1] <= cur_weight:

                # compare the max excluding/including current item and keep the biggest value
                exclude_item = matrix[item - 1][cur_weight]
                include_item = values[item - 1] + matrix[item - 1][cur_weight - weights[item - 1]]

                matrix[item][cur_weight] = max(exclude_item, include_item)
            else:
                # if the item is too heavy, don't include it
                matrix[item][cur_weight] = matrix[item - 1][cur_weight]

    # max is located in the bottom-right corner of table
    max_value = matrix[num_items][capacity]

    if show_output:
        print(f"Maximum value achievable: {max_value}")

    return max_value

def main():
    test_cases = [
        {"name": "Small Input", "weights": [1, 2, 3], "values": [6, 10, 12], "capacity": 5},
        {"name": "Medium Input", "weights": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], "values": [22, 33, 44, 55, 66, 77, 88, 99, 110, 120], "capacity": 150},
        {"name": "Edge Case: Empty Input", "weights": [], "values": [], "capacity": 10},
    ]

    print("--- 0/1 Knapsack Test Cases ---\n")
    for test in test_cases:
        print(f"Test {test['name']}")
        print(f"Capacity: {test['capacity']}")
        print(f"Weights:  {test['weights']}")
        print(f"Values:   {test['values']}")

        # function call
        knapsack(test["weights"], test["values"], test["capacity"])

        print("-------------------------------\n")

    experimental_eval()

if __name__ == "__main__":
    main()
