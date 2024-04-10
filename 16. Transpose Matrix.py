from typing import List

class Solution:
  def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
      # Get the dimensions of the matrix
      m = len(matrix)
      n = len(matrix[0])

      # Initialize a new matrix to store the transpose
      transpose_matrix = [[0 for _ in range(m)] for _ in range(n)]

      # Iterate through the matrix and populate the transpose_matrix
      for i in range(m):
          for j in range(n):
              transpose_matrix[j][i] = matrix[i][j]

      return transpose_matrix

