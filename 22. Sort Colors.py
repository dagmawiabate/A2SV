from typing import List

class Solution:
  def sortColors(self, nums: List[int]) -> None:
    # Initialize pointers for the red, white, and blue sections
    red, white, blue = 0, 0, len(nums) - 1
    
    # Iterate through the array
    while white <= blue:
        if nums[white] == 0:
            # If current element is red, swap it with the element at red pointer
            nums[red], nums[white] = nums[white], nums[red]
            # Move red pointer to the right
            red += 1
            # Move white pointer to the right (as red and white sections are sorted)
            white += 1
        elif nums[white] == 1:
            # If current element is white, just move white pointer to the right
            white += 1
        else:
            # If current element is blue, swap it with the element at blue pointer
            nums[white], nums[blue] = nums[blue], nums[white]
            # Move blue pointer to the left
            blue -= 1

