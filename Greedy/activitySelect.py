# Authors: Chloe Robinson, Camila Fienco, Tiffany Shi
# Purpose: Implementing Activity Selection using Greedy Approach

def activitySelection(activities):
    activities.sort(key=lambda x: x[1])

    count = 0
    last_end = float('-inf')

    for start, end in activities:
        if start >= last_end:
            count += 1
            last_end = end

    return count

def main():
    #Test cases
    activities1 = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
    activities2 = [(1, 2), (3, 4), (5, 6), (7, 8)]
    activities3 = [(1, 3), (2, 4), (3, 5), (4, 6)]

    choice = input("Enter 1 for activities1, 2 for activities2, 3 for activities3: ")
    if choice == '1':
        result = activitySelection(activities1)
    elif choice == '2':
        result = activitySelection(activities2)
    elif choice == '3':
        result = activitySelection(activities3)

    print(result)

if __name__ == "__main__":
    main()
    