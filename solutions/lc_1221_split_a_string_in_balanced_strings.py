class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, curr = 0, 0
        for c in s:
            curr += -1 if c == "L" else 1
            if curr == 0:
                count += 1
        return count