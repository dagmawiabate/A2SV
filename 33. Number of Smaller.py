def count_smaller_elements(arr1, arr2):
  counts = []
  for num in arr2:
    count = binary_search(arr1, num)
    counts.append(count)
  return counts

def binary_search(arr, target):
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return left

# Reading input
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Counting smaller elements
counts = count_smaller_elements(arr1, arr2)

# Printing output
print(*counts)
