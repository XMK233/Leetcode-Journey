'''
155. Min Stack
Easy

1479

159

Favorite

Share
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
Accepted
263,939
Submissions
745,870
'''

class MinStack(object):
    nums = None
    smallest_index = None
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.smallest_index = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.nums == []:
            self.nums.append(x)
            self.smallest_index.append(0)
            return
        self.nums.append(x)
        latest_index = len(self.nums) - 1
        #x
        smallest_num = self.nums[self.smallest_index[-1]]
        if x < smallest_num:
            self.smallest_index.append(latest_index)
        else:
            self.smallest_index.append(self.smallest_index[-1])

    def pop(self):
        """
        :rtype: void
        """
        self.nums = self.nums[0:-1]
        self.smallest_index = self.smallest_index[0:-1]

    def top(self):
        """
        :rtype: int
        """
        return self.nums[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.nums[self.smallest_index[-1]]

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.push(-2)
obj.push(-4)
print(obj.nums, obj.smallest_index)
obj.pop()
print(obj.nums, obj.smallest_index)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()