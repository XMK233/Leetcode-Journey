class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) == 0:
            return None
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not bool(len(self.stack1) + len(self.stack2))

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
print(obj.pop())
print(obj.peek())
print(obj.empty())