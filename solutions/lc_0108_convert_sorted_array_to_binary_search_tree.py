# 108. Convert Sorted Array to Binary Search Tree
#
# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a binary search tree.
#
# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#
# Constraints:
#   • 1 <= nums.length <= 10^4
#   • -104 <= nums[i] <= 10^4
#   • nums is sorted in a strictly increasing order.
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import List, Optional
from auxiliary_data_structures.tree_node import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
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