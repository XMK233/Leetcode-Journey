class Solution:
    def palindrome(self, s):
        ## see whether s is palindrome
        if s == "":
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        length = len(a)
        #################################
        i, j = 0, length - 1
        while i < j:
            if a[i] == b[j] or b[i] == a[j]:
                i += 1
                j -= 1
            else:
                return self.palindrome(b[i:j + 1]) or self.palindrome(a[i:j + 1])
        return True

s = Solution()
# print(s.palindrome(""))
testStr = "abcd"
print(s.checkPalindromeFormation(
    "a",
    "b"
))
## 这种方法得到的复杂度是O(n).