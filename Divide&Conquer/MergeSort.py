# Authors: Chloe Robinson, Camila Fienco, Tiffany Shi
# Purpose: Implementing Merge Sort using Divide and Conquer

# Function: Merge Sort
# Input: An array
# Output: A sorted array
from math import floor

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

#Conquer
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
    sorted_array = [1, 2, 34, 45, 59, 102]
    unsorted_array = [42, 7, 91, 15, 63, 28, 84, 3, 56, 77, 19, 68, 24, 95, 11, 39, 72, 5, 88, 30]
    reverseSorted_array = [123, 86, 54, 32, 20, 12, 9]

    choice = input("1:Sorted array\n2:Unsorted array\n3:Reverse sorted array:\nEnter: ")
    if choice == '1':
        result = merge_sort(sorted_array)
    elif choice == '2':
        result = merge_sort(unsorted_array)
    elif choice == '3':
        result = merge_sort(reverseSorted_array)

    print(result)

if __name__ == "__main__":
    main()