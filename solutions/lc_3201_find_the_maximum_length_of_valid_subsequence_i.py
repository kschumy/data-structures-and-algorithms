# 3201. Find the Maximum Length of Valid Subsequence I
#
# You are given an integer array nums.
# A subsequence 'sub' of nums with length x is called valid if it satisfies:
#     (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == 
#     (sub[x - 2] + sub[x - 1]) % 2.
#
# Return the length of the longest valid subsequence of nums.
#
# A subsequence is an array that can be derived from another array by deleting
# some or no elements without changing the order of the remaining elements.
#
# Example 1:
# Input: nums = [1,2,3,4]
# Output: 4
# Explanation:
# The longest valid subsequence is [1, 2, 3, 4].
#
# Example 2:
# Input: nums = [1,2,1,1,2,1,2]
# Output: 6
# Explanation:
# The longest valid subsequence is [1, 2, 1, 2, 1, 2].
#
# Example 3:
# Input: nums = [1,3]
# Output: 2
# Explanation:
# The longest valid subsequence is [1, 3].
#
# Constraints:
#     • 2 <= nums.length <= 2 * 10^5
#     • 1 <= nums[i] <= 10^7
#
# Difficulty: Medium
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        prev_is_even = nums[0] % 2 == 0
        even_count = int(prev_is_even)
        alternating_count = 1
        for i in range(1, len(nums)):
            curr_is_even = nums[i] % 2 == 0
            if curr_is_even:
                even_count += 1
            if prev_is_even != curr_is_even:
                alternating_count += 1
            prev_is_even = curr_is_even
        odd_count = len(nums) - even_count
        return max(even_count, odd_count, alternating_count)
