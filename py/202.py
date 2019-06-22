'''
202. Happy Number
Easy

886

228

Favorite

Share
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

## https://www.cnblogs.com/grandyang/p/4447233.html
## the number will iterate. Like, for example, 11 -> 2 -> -> 4 -> .... -> 4. Come to 4 again.
## So we use a hash table to see if a number is iterated.
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        step = {}

        num = n
        while True:
            hehe = 0
            while True:
                hehe += (num - num // 10 * 10) ** 2
                num //= 10
                if num == 0:
                    break
            num = hehe
            if hehe in step:
                return False
            elif hehe == 1:
                return True
            else:
                step[hehe] = 1

s = Solution()
print(s.isHappy(19))