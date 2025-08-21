## The Backtracking Template

### Example 1

```python
def backtrack(partial_solution, remaining_choices):
	# Base case: check if we have a complete solution
  if is_complete(partial_solution):
    if is_valid(partial_solution):
      solutions.append(partial_solution.copy())
    return
  
  for choice in remaining_choices:
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
