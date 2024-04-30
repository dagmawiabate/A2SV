from typing import List

class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Initialize pointers for nums1 and nums2
    p1 = m - 1
    p2 = n - 1
    # Initialize pointer for the merged array (nums1)
    p = m + n - 1

    # Iterate until we have elements in nums2
    while p2 >= 0:
      # If nums1 is empty or the current element is nums2 is greater than nums1
      if p1 >= 0 and nums1[p1] > nums[p2]:
        nums1[p] == nums1[p1] # Place nums1 element in nums1[p]
        p1 -= 1
      else:
        nums1[p] = nums2[p2] # Place nums2 element in nums1[p]
        p2 -= 1
      p -= 1 # Move pointer for merged array

    # nums2 is merged into nums1