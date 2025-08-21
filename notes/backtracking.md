## What is Backtracking?

At its core, backtracking is a general algorithmic technique used to solve problems that require exploring multiple possibilities and “undoing” choices when they lead to dead ends.

Think of it like a maze:
* You walk down a path (make a choice).
* If you hit a dead end (invalid state), you backtrack to the last decision point and try another path.
* Eventually, you either find a valid solution or prove none exists.

Backtracking incrementally builds candidates for solutions, abandons (“backtracks”) a candidate as soon as it determines that the candidate cannot possibly lead to a valid solution.

## Key Ideas
**Recursion drives the exploration**  
Each recursive call tries the next decision.

**Backtracking undoes a decision**  
Without this step, you can’t explore alternative paths.

**Pruning makes it efficient**  
Don’t explore paths that clearly cannot lead to a solution.

**Exponential complexity**  
Backtracking often explores many possibilities, but pruning reduces unnecessary work.

## The Backtracking Template

### Example 1

```python
def backtrack(partial_solution, remaining_choices):
	# Base case: check if we have a complete solution
  	if is_complete(partial_solution):
    	if is_valid(partial_solution):
			# Found a valid solution
			solutions.append(partial_solution.copy())
    return

	# Try each possible choice
  for choice in remaining_choices:
		# Make the choice
    partial_solution.append(choice)
      
    # Pruning: skip if this choice makes solution invalid
    if not is_promising(partial_solution, choice):
      continue
    
    # Recursively explore with this choice
    backtrack(partial_solution, get_next_choices(choice, remaining_choices))
    
    # Backtrack: undo the choice
    partial_solution.pop()
```

### Example #2

```python
def backtrack(path, options):
  if goal_reached(path):
    record_solution(path)
    return

  for choice in options:
    if is_valid(choice, path):  # pruning
      path.append(choice)     # make a choice
      backtrack(path, new_options(choice))  # explore further
      path.pop()              # undo the choice (backtrack)
```

## Commmon Problem Types

### 1. Permutations
Generate all possible arrangements of elements.  
Example: All permutations of [1,2,3]  
Key insight: Each position gets filled with remaining choices

### 2. Combinations
Choose a subset of elements where order doesn't matter.  
Example: All 2-element combinations from [1,2,3,4]
Key insight: Avoid duplicates by maintaining order

### 3. Subsets
Generate all possible subsets (power set).  
Example: All subsets of [1,2,3]
Key insight: For each element, choose to include it or not

### 4. Constraint Satisfaction
Find arrangements that satisfy given constraints.  
Example: N-Queens, Sudoku  
Key insight: Check constraints before proceeding

### 5. Path Finding
Find paths through a grid or graph.  
Example: Word search, maze solving  
Key insight: Mark visited cells and unmark when backtracking


## Classic Problems with Solutions

### 1. Generate All Permutations

**Problem**: Generate all permutations of a list of numbers.

#### Approach #1
```python
def permute(nums):
	result = []
    
	def backtrack(current_perm, remaining):
		# Base case: no more numbers to place
		if not remaining:
			result.append(current_perm.copy())
			return
			
		# Try each remaining number in the current position
		for i, num in enumerate(remaining):
			current_perm.append(num) # Make choice
			new_remaining = remaining[:i] + remaining[i+1:]
			backtrack(current_perm, new_remaining) # Recursion
			current_perm.pop() # Backtrack
	
	backtrack([], nums)
	return result

# Example usage
print(permute([1, 2, 3]))
# Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

#### Approach #2
```python
def permute(nums):
	result= []
	used = [False]*len(nums)

	def backtrack(path):
		if len(path) == len(nums):
			result.append(path[:])
			return
		for i in range(len(nums)):
			if used[i]:
				continue
			used[i] = True
			path.append(nums[i])
			backtrack(path)
			path.pop()
			used[i] = False
backtrack([])
return result
```

### 2. Generate All Combinations

##### Example #1

**Problem**: Generate all k-length combinations from n numbers.

```python
def combine(n, k):
    result = []
    
    def backtrack(start, current_combo):
        # Base case: we have k numbers
        if len(current_combo) == k:
            result.append(current_combo.copy())
            return
        
        # Try numbers from start to n
        for i in range(start, n + 1):
            current_combo.append(i) # Make choice
            backtrack(i + 1, current_combo) # Recurse with next starting position
            current_combo.pop() # Backtrack
    
    backtrack(1, [])
    return result

# Example usage
print(combine(4, 2))
# Output: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
```

##### Example #2

**Problem**: Generate all subsets of [1,2,3]

```
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])  # record current subset
        for i in range(start, len(nums)):
            path.append(nums[i])     # choose
            backtrack(i+1, path)     # explore
            path.pop()               # un-choose
    backtrack(0, [])
    return result

```

### 3. N-Queens Problem

**Problem**: Place N queens on an N×N chessboard so they don't attack each other.

#### Approach #1

```python
def solve_n_queens(n):
    result = []
    board = ['.' * n for _ in range(n)]
    
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal (top-left to bottom-right)
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check diagonal (top-right to bottom-left)
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(row):
        # Base case: placed all queens
        if row == n:
            result.append([row[:] for row in board])
            return
        
        # Try placing queen in each column of current row
        for col in range(n):
            if is_safe(row, col):
				# Make choice
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                
                # Recurse
                backtrack(row + 1)
                
                # Backtrack
                board[row] = board[row][:col] + '.' + board[row][col+1:]
    
    backtrack(0)
    return result
```

#### Approach #2

```
def solveNQueens(n):
    result = []
    cols, diag1, diag2 = set(), set(), set()  # track used columns & diagonals
    
    def backtrack(row, path):
        # Base case: all queens placed
        if row == n:
            result.append(["".join(r) for r in path])  # convert board to strings
            return
        
        # Try placing a queen in each column of current row
        for col in range(n):
            # Skip if column or diagonal already occupied
            if col in cols or (row-col) in diag1 or (row+col) in diag2:
                continue
            
            # Place queen
            row_str = ["." for _ in range(n)]
            row_str[col] = "Q"
            path.append(row_str)
            cols.add(col)
			diag1.add(row-col)
			diag2.add(row+col)
            
            # Recurse to next row
            backtrack(row+1, path)
            
            # Backtrack: remove queen and free constraints
            path.pop()
            cols.remove(col)
			diag1.remove(row-col)
			diag2.remove(row+col)
    
    backtrack(0, [])
    return result

```

### 4. Word Search in Grid

**Problem**: Find if a word exists in a 2D grid of letters.

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def backtrack(r, c, index):
        # Base case: found the word
        if index == len(word):
            return True
        
        # Out of bounds or wrong character
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            board[r][c] != word[index]):
            return False
        
        # Mark current cell as visited
        temp = board[r][c]
        board[r][c] = '#'
        
        # Explore all 4 directions
        found = (backtrack(r+1, c, index+1) or
                backtrack(r-1, c, index+1) or
                backtrack(r, c+1, index+1) or
                backtrack(r, c-1, index+1))
        
        # Backtrack: restore original character
        board[r][c] = temp
        
        return found
    
    # Try starting from each cell
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    
    return False
```

---

## Optimization Techniques

### 1. Early Pruning
Stop exploring a branch as soon as you know it can't lead to a solution.

```python
# Instead of this:
def bad_backtrack(partial_solution):
    if len(partial_solution) == target_length:
        if is_valid(partial_solution):
            solutions.append(partial_solution.copy())
        return
    
    for choice in choices:
        partial_solution.append(choice)
        bad_backtrack(partial_solution)
        partial_solution.pop()

# Do this:
def good_backtrack(partial_solution):
    # Early termination
    if not is_promising(partial_solution):
        return
    
    if len(partial_solution) == target_length:
        solutions.append(partial_solution.copy())
        return
    
    for choice in choices:
        partial_solution.append(choice)
        good_backtrack(partial_solution)
        partial_solution.pop()
```

### 2. Constraint Propagation
Use problem-specific knowledge to reduce the search space.

### 3. Variable Ordering
Choose variables/positions in an order that leads to earlier pruning.

### 4. Value Ordering
Try values that are more likely to lead to solutions first.

---

## Common Pitfalls

### 1. Forgetting to Backtrack
```python
# WRONG - forgot to remove choice AND forgot to copy
def wrong_backtrack(current, remaining):
    if not remaining:
        result.append(current)  # BUG 1: No .copy() - will store reference
        return
    
    for choice in remaining:
        current.append(choice)  # Make choice
        new_remaining = [x for x in remaining if x != choice]
        wrong_backtrack(current, new_remaining)
        # BUG 2: Missing current.pop() - forgot to backtrack!

# CORRECT
def correct_backtrack(current, remaining):
    if not remaining:
        result.append(current.copy())
        return
    
    for choice in remaining:
        current.append(choice)
        new_remaining = [x for x in remaining if x != choice]
        correct_backtrack(current, new_remaining)
        current.pop()  # Backtrack
```

### 2. Modifying Shared State Incorrectly
```python
# WRONG - modifying the same list reference
result.append(current)

# CORRECT - create a copy
result.append(current.copy())
```

### 3. Not Handling Base Cases Properly
Always clearly define when you have a complete solution.

### 4. Infinite Recursion
Make sure your recursive calls are making progress toward the base case.
