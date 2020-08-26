class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head = 0
        tail = len(s) - 1
        while not (head > tail):
            tmp = s[head]
            s[head] = s[tail]
            s[tail] = tmp
            head += 1
            tail -= 1

s = Solution()
t = [i for i in "a"]
s.reverseString(t)
print(t)