def selection_sort(arr):
    # Traverse through all elements in the array
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Take input from the user
arr = list(map(int, input("Enter numbers separated by space: ").split()))

# Sort the array using selection sort
selection_sort(arr)

# Print the sorted array
print("Sorted array:", arr)
