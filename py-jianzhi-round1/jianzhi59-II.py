import queue
class MaxQueue:
    """1队列+1双端队列"""

    def __init__(self):
        self.queue = []#queue.Queue()
        self.deque = []#queue.deque()

    def max_value(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1
        # return self.deque[0] if self.deque else -1 或者这样写

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.deque: return -1
        ans = self.queue[0] #.get()
        self.queue.pop(0)
        if ans == self.deque[0]:
            self.deque.pop(0)#left()
        return ans

# 作者：z1m
# 链接：https: // leetcode - cn.com / problems / dui - lie - de - zui - da - zhi - lcof / solution / ru - he - jie - jue - o1 - fu - za - du - de - api - she - ji - ti - by - z1m /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
## 链接的那个解析非常好. 非常好理解, 值得记住.