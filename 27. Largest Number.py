from typing import List
from functools import cmp_to_key

class Solution:

  def largestNumber(self, nums: List[int]) -> str:
      # Custom comparator function to compare concatenated strings
      def compare(a, b):
          return int(b + a) - int(a + b)

      # Convert integers to strings
      nums_str = [str(num) for num in nums]
      
      # Sort the numbers using the custom comparator
      nums_str.sort(key=cmp_to_key(compare))
      
      # Handle case where all numbers are 0
      if nums_str[0] == '0':
          return '0'
      
      # Concatenate the sorted numbers and return as string
      return ''.join(nums_str)