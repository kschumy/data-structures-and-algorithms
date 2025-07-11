# 94. Binary Tree Inorder Traversal (Iterative Solution)
#
# Given the root of a binary tree, return the inorder traversal of its nodes' 
# values.
#
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]
#
# Example 3:
# Input: root = []
# Output: []
#
# Example 4:
# Input: root = [1]
# Output: [1]
#
# Constraints:
#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/

from auxiliary_data_structures.tree_node import TreeNode
from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        vals = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            vals.append(curr.val)
            curr = curr.right
        return vals