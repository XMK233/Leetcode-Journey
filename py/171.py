'''

171. Excel Sheet Column Number
Easy

491

89

Favorite

Share
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        number = 0
        for i in reversed(range(length)):
            _ = length - 1 - i
            a = s[_]
            number += (ord(a) - 64) * 26 ** i
        return number

s = Solution()
print(s.titleToNumber("ZY"))