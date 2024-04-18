def can_reduce_to_one():
    t = int(input())  # Number of test cases
    results = []

    for _ in range(t):
        n = int(input())  # Length of array
        a = sorted(map(int, input().split()))  # Sorted array elements
        for i in range(1, n):
            if a[i] - a[i - 1] > 1:
                results.append("NO")  # If the difference between adjacent elements is greater than 1, it's not possible to reduce to one
                break
        else:
            results.append("YES")

    for result in results:
        print(result)

can_reduce_to_one()
