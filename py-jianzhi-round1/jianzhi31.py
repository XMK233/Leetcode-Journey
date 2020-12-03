class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        if len(pushed) == 0:
            return True
        ## 假定两个数组都非空
        pushIndex = 1
        popIndex = 0
        stack = []
        stack.append(pushed[0])
        while popIndex < len(popped):
            if stack[-1] != popped[popIndex]:
                if pushIndex >= len(pushed):
                    return False
                else:
                    stack.append(pushed[pushIndex])
                    pushIndex += 1
            else:
                popIndex += 1
                stack.pop(-1)
                if len(stack) == 0:
                    if pushIndex < len(pushed):
                        stack.append(pushed[pushIndex])
        return True

s = Solution()
print(s.validateStackSequences(pushed = [1,0], popped = [1, 0]))
## 具体的思路是，利用一个栈，来复盘压入和弹出的顺序。
## 参考了一下推荐思路，然后自己实现了。
## 实现的不太好。
