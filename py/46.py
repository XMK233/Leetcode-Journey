class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, res, [])
        return res

    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])

### 为什么dfs要这样写?
#### 你仔细想想啊. 如果我先把path加进res里面, 那么我是要把已经加入res里面的path给延长的吧?
#### 那不就很麻烦了嘛...你还的去找, 或者是浪费一部分空间.
#### 所以啊, 这个方法巧妙就在于, 它是将一条路探到底了, 也就是当前的nums是空集了, 才把path加入到res里面.