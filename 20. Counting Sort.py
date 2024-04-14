def countingSort(arr):
    # Write your code here
    # Create an array to store frequencies
    freq = [0] * 100
    
    # Count occurrences of each element
    for num in arr:
        freq[num] += 1
    
    return freq

