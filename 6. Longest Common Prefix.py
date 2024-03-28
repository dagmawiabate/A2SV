from typing import List

class Solution: 
  def longest_common_prefix(self, strs: List[str]) -> str:
      if not strs:
          return ""

      # Sort the strings to ensure that the common prefix will be between the first and the last string
      strs.sort()

      # Find the common prefix between the first and the last string
      prefix = ""
      for i in range(min(len(strs[0]), len(strs[-1]))):
          if strs[0][i] == strs[-1][i]:
              prefix += strs[0][i]
          else:
              break

      return prefix

