def countSwaps(a):
    num_swaps = 0
    n = len(a)
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                num_swaps += 1
    
    print("Array is sorted in", num_swaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])

