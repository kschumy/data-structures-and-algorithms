# 3304. Find the K-th Character in String Game I
#
# Alice and Bob are playing a game. Initially, Alice has a string word = "a".
#
# You are given a positive integer k.
#
# Now Bob will ask Alice to perform the following operation forever:
# Generate a new string by changing each character in word to its next character
# in the English alphabet, and append it to the original word.
# 
# For example, performing the operation on "c" generates "cd" and performing the
# operation on "zb" generates "zbac".
#
# Return the value of the kth character in word, after enough operations have 
# been done for word to have at least k characters.
#
# Note that the character 'z' can be changed to 'a' in the operation.
#
# Example 1:
# Input: k = 5
# Output: "b"
# Explanation: Initially, word = "a". We need to do the operation three times:
#     Generated string is "b", word becomes "ab".
#     Generated string is "bc", word becomes "abbc".
#     Generated string is "bccd", word becomes "abbcbccd".
#
# Example 2:
# Input: k = 10
# Output: "c"
#
# Constraints:
#     1 <= k <= 500
#
# Daily Question: 07/02/2025
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i

class Solution:
    def kthCharacter(self, k: int) -> str:
        word = [97] # "a"
        while len(word) < k:
            start_len = len(word)
            for i in range(start_len):
                # The question has too low of a constraint on k. Even when k is
                # maxed out at 500, you never reach "z", so technically you 
                # don't need to solve for this case. But if the max of k was
                # higher and did allow for this, this line should be used 
                # instead of the one below:
                # word.append((word[i] - 97 + 1) % 26 + 97)
                word.append(word[i] + 1)
        return chr(word[k - 1])
