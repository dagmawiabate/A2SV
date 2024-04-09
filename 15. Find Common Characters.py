from typing import List
from collections import Counter
class Solution:
  def commonChars(self, nums: List[int]) -> List[int]:
      # Initialize a Counter for the first word
      common = Counter(words[0])
      
      # Iterate through the rest of the words
      for word in words[1:]:
          # Update the common Counter by taking the intersection with the Counter of the current word
          common &= Counter(word)
      
      # Convert the Counter to a list of characters, considering the duplicates
      result = []
      for char, count in common.items():
          result.extend([char]*count)
      
      return result
