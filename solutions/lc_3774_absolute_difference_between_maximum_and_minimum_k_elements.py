# https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/description/

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        return sum(nums[n - i - 1] - nums[i] for i in range(k))