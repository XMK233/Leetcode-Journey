class NumArray:
    def __init__(self, nums):
        ## 创建中间结果数组. 数组的长度比nums长1. 为的是存储一个0值.
        ## 储存一个0值的目的是为了应对i, j都是0的情况.
        self.nums = nums
        self.intermediateList = [0]
        for num in self.nums:
            self.intermediateList.append(self.intermediateList[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        ## 用到j位置的nums子数组的累加和减去到i-1位置的nums子数组的累加和.
        ## 所以, __init__方法里面存储中间结果的意义就体现出来了.
        return (self.intermediateList[j + 1] - self.intermediateList[i])

# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0,5)
print(param_1)