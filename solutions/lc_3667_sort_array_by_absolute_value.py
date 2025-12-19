from typing import List

class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=abs)