# tests/test_set_matrix_zeroes_extra_space.py
import pytest
import random
from typing import List

from solutions.LC_0073_Set_Matrix_Zeroes_extra_space import SetZeroesExtraSpace

solver = SetZeroesExtraSpace()

def test_example_1():
    """Test case from Example 1 of the problem description."""
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    expected = [[1,0,1],[0,0,0],[1,0,1]]
    solver.solve(matrix)
    assert matrix == expected

def test_example_2():
    """Test case from Example 2 of the problem description."""
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    expected = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    solver.solve(matrix)
    assert matrix == expected

def test_no_zeros():
    """Test case where the matrix contains no zeros. Should remain unchanged."""
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    expected = [[1,2,3],[4,5,6],[7,8,9]]
    solver.solve(matrix)
    assert matrix == expected

def test_all_zeros():
    """Test case where the entire matrix is already zeros."""
    matrix = [[0,0],[0,0]]
    expected = [[0,0],[0,0]]
    solver.solve(matrix)
    assert matrix == expected

def test_single_zero_middle():
    """Test case with a single zero in the middle of the matrix."""
    matrix = [[1,2,3],[4,0,6],[7,8,9]]
    expected = [[1,0,3],[0,0,0],[7,0,9]]
    solver.solve(matrix)
    assert matrix == expected

def test_zero_top_left_corner():
    """Test case with a zero in the top-left corner."""
    matrix = [[0,1,2],[3,4,5],[6,7,8]]
    expected = [[0,0,0],[0,4,5],[0,7,8]]
    solver.solve(matrix)
    assert matrix == expected

def test_zero_top_right_corner():
    """Test case with a zero in the top-right corner."""
    matrix = [[1,2,0],[3,4,5],[6,7,8]]
    expected = [[0,0,0],[3,4,0],[6,7,0]]
    solver.solve(matrix)
    assert matrix == expected

def test_zero_bottom_left_corner():
    """Test case with a zero in the bottom-left corner."""
    matrix = [[1,2,3],[4,5,6],[0,7,8]]
    expected = [[0,2,3],[0,5,6],[0,0,0]]
    solver.solve(matrix)
    assert matrix == expected

def test_zero_bottom_right_corner():
    """Test case with a zero in the bottom-right corner."""
    matrix = [[1,2,3],[4,5,6],[7,8,0]]
    expected = [[1,2,0],[4,5,0],[0,0,0]]
    solver.solve(matrix)
    assert matrix == expected

def test_multiple_zeros_scattered():
    """Test case with multiple zeros scattered throughout the matrix."""
    matrix = [[1,0,1,1],[1,1,1,0],[1,1,0,1],[1,1,1,1]]
    expected = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
    solver.solve(matrix)
    assert matrix == expected

def test_multiple_zeros_intersecting():
    """Test case with zeros causing intersecting zeroed rows/columns."""
    matrix = [[1,1,1,1],[1,0,1,1],[1,1,1,0],[1,1,1,1]]
    expected = [[1,0,1,0],[0,0,0,0],[0,0,0,0],[1,0,1,0]]
    solver.solve(matrix)
    assert matrix == expected

def test_1x1_matrix_zero():
    """Test case for a 1x1 matrix with a zero."""
    matrix = [[0]]
    expected = [[0]]
    solver.solve(matrix)
    assert matrix == expected

def test_1x1_matrix_non_zero():
    """Test case for a 1x1 matrix with a non-zero element."""
    matrix = [[5]]
    expected = [[5]]
    solver.solve(matrix)
    assert matrix == expected

def test_1xN_matrix_zero():
    """Test case for a 1-row matrix with a zero."""
    matrix = [[1,0,1,5,9]]
    expected = [[0,0,0,0,0]]
    solver.solve(matrix)
    assert matrix == expected

def test_Mx1_matrix_zero():
    """Test case for a 1-column matrix with a zero."""
    matrix = [[1],[0],[1],[5],[9]]
    expected = [[0],[0],[0],[0],[0]]
    solver.solve(matrix)
    assert matrix == expected

def test_zero_in_first_row_only():
    """Test case where the only zero is in the first row (non-first column)."""
    matrix = [[1,2,0,4],[5,6,7,8],[9,10,11,12]]
    expected = [[0,0,0,0],[5,6,0,8],[9,10,0,12]]
    solver.solve(matrix)
    assert matrix == expected

def test_zero_in_first_col_only():
    """Test case where the only zero is in the first column (non-first row)."""
    matrix = [[1,2,3,4],[0,6,7,8],[9,10,11,12]]
    expected = [[0,2,3,4],[0,0,0,0],[0,10,11,12]]
    solver.solve(matrix)
    assert matrix == expected

def test_large_matrix_sparse_zeros():
    """
    Test case with a large matrix (200x200, near max constraints) and a few strategically placed zeros.
    This tests performance and correctness on a larger scale.
    """
    m, n = 200, 200
    # Initialize matrix with random non-zero values
    matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]

    # Place a few zeros at specific locations
    zeros_to_place = [(10, 20), (50, 150), (199, 0), (0, 199), (100, 100), (0,0)]
    for r, c in zeros_to_place:
        matrix[r][c] = 0

    # Create a deep copy to calculate the expected output based on the original zero positions
    original_matrix_copy = [row[:] for row in matrix]
    
    # Manually determine which rows and columns should be zeroed
    rows_to_zero = set()
    cols_to_zero = set()
    for r in range(m):
        for c in range(n):
            if original_matrix_copy[r][c] == 0:
                rows_to_zero.add(r)
                cols_to_zero.add(c)

    # Construct the expected matrix
    expected_matrix = [[0 for _ in range(n)] for _ in range(m)]
    for r in range(m):
        for c in range(n):
            if r not in rows_to_zero and c not in cols_to_zero:
                expected_matrix[r][c] = original_matrix_copy[r][c]

    solver.solve(matrix)
    assert matrix == expected_matrix

def test_large_matrix_diagonal_zeros():
    """
    Test case with a large matrix (200x200) and zeros along a diagonal.
    This tests the interaction of multiple zeroed rows/columns and can stress the flagging mechanism.
    """
    m, n = 200, 200
    matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]

    # Place zeros along the main diagonal
    for i in range(min(m, n)):
        matrix[i][i] = 0
    
    # Create a deep copy to calculate the expected output
    original_matrix_copy = [row[:] for row in matrix]
    
    # Manually determine which rows and columns should be zeroed
    rows_to_zero = set()
    cols_to_zero = set()
    for r in range(m):
        for c in range(n):
            if original_matrix_copy[r][c] == 0:
                rows_to_zero.add(r)
                cols_to_zero.add(c)

    # Construct the expected matrix
    expected_matrix = [[0 for _ in range(n)] for _ in range(m)]
    for r in range(m):
        for c in range(n):
            if r not in rows_to_zero and c not in cols_to_zero:
                expected_matrix[r][c] = original_matrix_copy[r][c]

    solver.solve(matrix)
    assert matrix == expected_matrix
