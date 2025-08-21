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
    if not is_promising(partial_solution):
      partial_solution.pop()  # backtrack
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
