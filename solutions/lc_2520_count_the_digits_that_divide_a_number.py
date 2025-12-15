from collections import Counter

class Solution:
    def countDigits(self, num: int) -> int:
        digit_freq = Counter(str(num))
        # Technically, removing "0" is not needed because the 
        # constraints say the input will not contain a "0", but
        # I have included it for completeness.
        if "0" in digit_freq:
            del digit_freq["0"]
        
        count = 0
        for k, v in digit_freq.items():
            if num % int(k) == 0:
                count += v
        return count