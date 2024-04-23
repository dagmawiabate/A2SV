def count_elements_less_or_equal_to(sequence, z):
    count = 0
    for num in sequence:
        if num <= z:
            count += 1
    return count


def find_z(sequence, k):
    max_value = max(sequence)
    if max_value < 10**9:
        right = max_value + 1
    else:
        return -1
    # unique_elements = sorted(set(sequence))
    # if len(unique_elements) < k:
    #     return -1

    left, right = 1, 10**9
    while left < right:
        mid = (left + right) // 2
        count = count_elements_less_or_equal_to(sequence, mid)
        if count == k:
            return mid
        elif count < k:
            left = mid + 1
        else:
            right = mid
    return -1


# Input
n, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Output
result = find_z(sequence, k)
print(result)
