'''
172. Factorial Trailing Zeroes
Easy

439

632

Favorite

Share
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
https://unnamed42.github.io/2015-12-03-Leetcode-172-Factorial-Trailing-Zeroes.html
'''
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # p = 1
        num_5 = 0
        # num_2 = 0
        num = 0
        while(True):
            num += n // 5
            n = n // 5
            if n < 5:
                break
        return num

s = Solution()
print(s.trailingZeroes(25))