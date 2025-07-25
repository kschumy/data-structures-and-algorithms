# 1249. Minimum Remove to Make Valid Parentheses
#
# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any 
# positions ) so that the resulting parentheses string is valid and return any 
# valid string.
#
# Formally, a parentheses string is valid if and only if:
#   • It is the empty string, contains only lowercase characters, or
#   • It can be written as AB (A concatenated with B), where A and B are valid 
#     strings, or
#   • It can be written as (A), where A is a valid string.
#
# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#
# Example 2:
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
#
# Example 3:
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#
# Constraints:
#   • 1 <= s.length <= 10^5
#   • s[i] is either '(' , ')', or lowercase English letter.
#
# Difficulty: Medium
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_parentheses_indexes = []
        s_arr = list(s)
        for i in range(len(s_arr)):
            if s_arr[i] == "(":
                open_parentheses_indexes.append(i)
                s_arr[i] = ""
            elif s_arr[i] == ")":
                if open_parentheses_indexes:
                    s_arr[open_parentheses_indexes.pop()] = "("
                else:
                    s_arr[i] = ""
        return "".join(s_arr)
