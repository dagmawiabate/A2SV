from typing import List

class Solution:
  def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
      n = len(grid)
      max_local = []
      
      for i in range(n - 2):
          row = []
          for j in range(n - 2):
              submatrix = [grid[i+k][j:j+3] for k in range(3)]
              max_value = max(max(row) for row in submatrix)
              row.append(max_value)
          max_local.append(row)
      
      return max_local