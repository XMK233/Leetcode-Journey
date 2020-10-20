class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackGeneral = []
        self.stackMin = []

    def push(self, x: int) -> None:
        self.stackGeneral.append(x)
        if len(self.stackMin) == 0:
            self.stackMin.append(x)
        else:
            self.stackMin.append(min(x, self.stackMin[-1]))

    def pop(self) -> None:
        if len(self.stackGeneral) == 0:
            pass
        else:
            self.stackMin.pop(-1)
            self.stackGeneral.pop(-1)

    def top(self) -> int:
        return None if len(self.stackGeneral) == 0 else self.stackGeneral[-1]

    def min(self) -> int:
        return None if len(self.stackMin) == 0 else self.stackMin[-1]

### 思路非常简单，就是如果新加入一个数字，那么min数组也要对应增加一个当前最小值。

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()