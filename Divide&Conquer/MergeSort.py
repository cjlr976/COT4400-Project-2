# Authors: Chloe Robinson, Camila Fienco
# Purpose: Implementing Merge Sort using Divide and Conquer

# Function: Merge Sort
# Input: An unsorted array
# Output: A sorted array
def merge_sort(arr):
    #Base case
    if len(arr) <= 1:
        return arr

    #Divide recursively
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    #Conquer
    return merge(left_half, right_half)

#Combine
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
    unsorted_array = [5, 42, 14, 20, 1, 24, 76, 58]
    reverseSorted_array = [123, 86, 54, 32, 20, 12, 9]

    choice = input("Enter 1 for sorted array, 2 for unsorted array, 3 for reverse sorted array: ")
    if choice == '1':
        result = merge_sort(sorted_array)
    elif choice == '2':
        result = merge_sort(unsorted_array)
    elif choice == '3':
        result = merge_sort(reverseSorted_array)

    print(result)

if __name__ == "__main__":
    main()