from typing import List

class Solution:
  def targetIndices(self, nums: List[int], target: int) -> List[int]:
    target_indices = []

    for index, value in enumerate(sorted(nums)):
        if target == value:
            target_indices.append(index)
    
    return target_indices

