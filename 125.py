'''
125. Valid Palindrome
Easy

513

1435

Favorite

Share
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
Accepted
316,107
Submissions
1,052,733
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        if s == "":
            return True

        length = len(s)
        head = -1
        rear = length
        while True:
            while True:
                head += 1
                if head >= length or s[head].isalnum():
                    break
            while True:
                rear -= 1
                if rear < 0 or s[rear].isalnum():
                    break
            if head > rear:
                return True
            if s[head] != s[rear]:
                return False

s = Solution()
print(s.isPalindrome("race a car"))

