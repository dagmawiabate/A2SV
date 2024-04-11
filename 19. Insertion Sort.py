def insertionSort1(n, arr):
    e = arr[-1]  # Store the value of the unsorted element
    idx = n - 2  # Start comparing from the second last element

    while idx >= 0 and arr[idx] > e:
        arr[idx + 1] = arr[idx]  # Shift elements to the right
        print(*arr)  # Print the array after each shift
        idx -= 1

    arr[idx + 1] = e  # Insert the unsorted element at the correct position
    print(*arr)  # Print the final sorted array