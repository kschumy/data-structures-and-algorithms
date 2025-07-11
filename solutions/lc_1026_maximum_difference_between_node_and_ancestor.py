# 1026. Maximum Difference Between Node and Ancestor
#
# Given the root of a binary tree, find the maximum value v for which there exist
# different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
# A node a is an ancestor of b if either: any child of a is equal to b or any 
# child of a is an ancestor of b.
#
# Example 1:
# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are below:
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the max value of 7 is obtained by |8 - 1| = 7.
#
# Example 2:
# Input: root = [1,null,2,null,0,3]
# Output: 3
#
# Constraints:
#     The number of nodes in the tree is in the range [2, 5000].
#     0 <= Node.val <= 10^5
#
# Difficulty: Medium
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor

from typing import Optional
from auxiliary_data_structures.tree_node import TreeNode

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # Tuple elements at each index:
        #   [0] current node
        #   [1] LOWEST value in ancestor nodes
        #   [2] HIGHEST value in ancestor nodes
        stack = [(root, root.val, root.val)]
        biggest_diff = 0
        
        while stack:
            node, lowest, highest = stack.pop()
            
            if node.val > highest:
                highest = node.val
                biggest_diff = max(biggest_diff, highest - lowest)
            elif node.val < lowest:
                lowest = node.val
                biggest_diff = max(biggest_diff, highest - lowest)
            
            if node.right:
                stack.append((node.right, lowest, highest))
            if node.left:
                stack.append((node.left, lowest, highest))
        
        return biggest_diff
