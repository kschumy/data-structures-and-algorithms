class Solution:
    def minimumChairs(self, s: str) -> int:
        total_chairs = 0
        available_chairs = 0
        for c in s:
            if c == "L":
                available_chairs += 1
            elif available_chairs > 0: # c == "E" and has available chair
                available_chairs -= 1
            else: # c == "E" but no available chair
                total_chairs += 1
        return total_chairs