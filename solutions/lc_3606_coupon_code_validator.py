# https://leetcode.com/problems/coupon-code-validator/description

import string
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        allowable_business_lines = set(["electronics", "grocery", "pharmacy", "restaurant"])
        allowable_chars = set(string.ascii_letters + string.digits + "_")

        valid_coupons = []
        for coupon, business, active in zip(code, businessLine, isActive):
            if (
                active and
                business in allowable_business_lines and
                len(coupon) > 0 and 
                all(c in allowable_chars for c in coupon)
            ):
                valid_coupons.append((business, coupon))
        
        valid_coupons.sort()
        return [vc for _, vc in valid_coupons]