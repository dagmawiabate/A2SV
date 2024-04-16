from typing import List

class Solution:
  def pancakeSort(self, arr: List[int]) -> List[int]:
      flips = []
      n = len(arr)
      # Iterate through the array from the end
      for i in range(n, 1, -1):
          # Find the index of the maximum element in the current unsorted portion
          max_index = arr.index(i)
          # If the maximum element is not already at its correct position
          if max_index != i - 1:
              # Flip the sub-array to move the maximum element to the beginning
              if max_index != 0:
                  flips.append(max_index + 1)
                  arr[:max_index + 1] = reversed(arr[:max_index + 1])
              # Flip the entire sub-array to move the maximum element to its correct position
              flips.append(i)
              arr[:i] = reversed(arr[:i])
      return flips
