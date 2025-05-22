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

from typing import List

class SetZeroesExtraSpace:
    def solve(self, matrix: List[List[int]]) -> None:
        rows_len, cols_len = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        # First pass: record which rows and columns need to be zeroed
        for r in range(rows_len):
            for c in range(cols_len):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # Second pass: zero out recorded rows
        for r in zero_rows:
            for c in range(cols_len):
                matrix[r][c] = 0

        # Third pass: zero out recorded columns
        for c in zero_cols:
            for r in range(rows_len):
                matrix[r][c] = 0