class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Iterate over rows
        for i in range(1, len(matrix)):
            # Iterate over columns
            for j in range(1, len(matrix[0])):
                # Check if the element is not equal to its top-left neighbor
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True
