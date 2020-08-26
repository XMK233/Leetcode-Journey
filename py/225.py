class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = []
        # self.top = None
        # self.length = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.storage.append(x)
        # self.top = self.storage[0]
        # self.length = len(self.storage)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        tmp = self.storage[-1]
        del self.storage[-1]
        return tmp

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.storage[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.storage) == 0:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(10)
# param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_3, param_4)

