# 73. Set Matrix Zeroes (medium)
#
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
#
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
# Constraints:
#   m == matrix.length
#   n == matrix[0].length
#   1 <= m, n <= 200
#   -231 <= matrix[i][j] <= 231 - 1
#
# https://leetcode.com/problems/set-matrix-zeroes/

class SetZeroesConstantSpace:
    def solve(self, matrix: List[List[int]]) -> None:
        rows_len = len(matrix)
        cols_len = len(matrix[0])
        first_row_has_zero = any(matrix[0][col] == 0 for col in range(cols_len))
        first_col_has_zero = any(matrix[row][0] == 0 for row in range(rows_len))

        # Use first row/col to flag zeros
        for row in range(1, rows_len):
            for col in range(1, cols_len):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Zero marked rows
        for row in range(1, rows_len):
            if matrix[row][0] == 0:
                for col in range(1, cols_len):
                    matrix[row][col] = 0

        # Zero marked columns
        for col in range(1, cols_len):
            if matrix[0][col] == 0:
                for row in range(1, rows_len):
                    matrix[row][col] = 0

        # Zero first row/col if needed
        if first_row_has_zero:
            for col in range(cols_len):
                matrix[0][col] = 0
        
        if first_col_has_zero:
            for row in range(rows_len):
                matrix[row][0] = 0