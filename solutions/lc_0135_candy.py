# 135. Candy
#
# There are n children standing in a line. Each child is assigned a rating value 
# given in the integer array ratings.
#
# You are giving candies to these children subjected to these requirements:
#    Each child must have at least one candy.
#    Children with a higher rating get more candies than their neighbors.
#
# Return the minimum number of candies you need to have to distribute the 
# candies to the children.
#
# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 
# 2, 1, 2 candies respectively.
#
# Example 2:
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 
# 1, 2, 1 candies respectively.The third child gets 1 candy because it satisfies
# the above two conditions.
#
# Constraints:
#   n == ratings.length
#   1 <= n <= 2 * 10^4
#   0 <= ratings[i] <= 2 * 10^4
#
# Difficulty: Hard
# https://leetcode.com/problems/candy/

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        total = candies[-1]
        for j in range(n - 2, -1 , -1):
            if ratings[j] > ratings[j + 1] and candies[j] <= candies[j + 1]:
                candies[j] = candies[j + 1] + 1 
            total += candies[j]
        return total

