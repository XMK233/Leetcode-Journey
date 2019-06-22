'''
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
'''

## bisection method. Because a square root of a number x
## will never be larger than x/2.
## another trick is that if you use mid**2 <= x, it may overflow
## use mid <= x / mid will be safer.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        else:
            return self.helper(1, x, x)

    def helper(self, low, high, x):
        mid = (low + high) // 2
        if mid <= x / mid and mid + 1 > x / (mid + 1):
            return int(mid)
        elif mid > x / mid:
            return int(self.helper(low, mid, x))
        elif mid + 1 <= x / (mid + 1):
            return int(self.helper(mid + 1, high, x))
        else:
            return 0


s = Solution()
s.mySqrt(16)