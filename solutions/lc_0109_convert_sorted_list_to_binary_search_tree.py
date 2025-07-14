# 109. Convert Sorted List to Binary Search Tree
#
# Given the head of a singly linked list where elements are sorted in ascending
# order, convert it to a binary search tree.
#
# Example 1:
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
# shown height balanced BST.
#
# Example 2:
# Input: head = []
# Output: []
#
# Constraints:
#   • The number of nodes in head is in the range [0, 2 * 10^4].
#   • -10^5 <= Node.val <= 10^5
#
# Difficulty: Medium
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

from typing import Optional

from auxiliary_data_structures.list_node import ListNode
from auxiliary_data_structures.tree_node import TreeNode

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        def builder(start_index, end_index):
            if start_index > end_index:
                return None
            elif start_index == end_index:
                return TreeNode(nums[start_index])

            mid_index = (start_index + end_index) // 2
            mid_node = TreeNode(nums[mid_index])
            mid_node.left = builder(start_index, mid_index - 1)
            mid_node.right = builder(mid_index + 1, end_index)
            return mid_node

        return builder(0, len(nums) - 1)