'''
https://www.nowcoder.com/practice/345e2ed5f81d4017bbb8cc6055b0b711?tpId=117&tqId=37751&rp=1&ru=%2Fta%2Fjob-code-high&qru=%2Fta%2Fjob-code-high%2Fquestion-ranking&tab=answerKey

题目描述
给出一个有n个元素的数组S，S中是否有元素a,b,c满足a+b+c=0？找出数组S中所有满足条件的三元组。
注意：
三元组（a、b、c）中的元素必须按非降序排列。（即a≤b≤c）
解集中不能包含重复的三元组。
例如，给定的数组 S = {-10 0 10 20 -10 -40},解集为(-10, 0, 10) (-10, -10, 20)

示例1
输入
复制
[-2,0,1,1,2]
返回值
复制
[[-2,0,2],[-2,1,1]]

https://blog.nowcoder.net/n/0cc3afd8375648a892f2cc07f86c93eb
参考上述链接, 我们将这个问题转为确定一个数字后的寻找两数的问题.

'''
class Solution:
    def threeSum(self , numbers ):
        nums = sorted(numbers)
        def findTwoNum(index1, index2, target):
            res = []
            idx1, idx2 = index1, index2
            while idx1 < idx2:
                currentSum = nums[idx1] + nums[idx2]
                if currentSum == target: ## curSum 刚好, 是最好的.
                    res.append([nums[idx1], nums[idx2]])
                    tmp = idx1
                    while idx1 < len(nums) and nums[idx1] == nums[tmp]: idx1 += 1
                    tmp = idx2
                    while idx2 >= 0 and nums[idx2] == nums[tmp]: idx2 -= 1
                elif currentSum < target: ## 如果cursum太小
                    tmp = idx1
                    while idx1 < len(nums) and nums[idx1] == nums[tmp]: idx1 += 1
                else: ## curSum太大怎么办?
                    tmp = idx2
                    while idx2 >= 0 and nums[idx2] == nums[tmp]: idx2 -= 1
            return res
        # write code here
        res = []
        index = 0
        while index < len(nums) - 2: ## 不要遍历到最后一个元素, 遍历到倒数第三个就够了.
            laterParts = findTwoNum(index1 = index + 1, index2 = len(nums) - 1, target = 0 - nums[index])
            if len(laterParts) == 0: ## 后续部分找不到目标值target
                pass
            else: ## 找到了的话, 就好了.
                for laterPart in laterParts:
                    laterPart.insert(0, nums[index])
                    res.append(laterPart)
            ## 下面两行是为了找没出现过的数字.
            tmp = index
            while index < len(nums) and nums[index] == nums[tmp]: index += 1
        return res


        # newNums = []
        # ## 排序后, 可能有重复的数字, 记得跳过
        # lastNum = None
        # for num in nums:
        #     if lastNum == None:
        #        lastNum = num
        #     elif lastNum == num:
        #         continue
        #     else:
        #         lastNum = num
        #     laterParts = findTwoNum()

s = Solution()
print(s.threeSum([-2,0,1,1,2]))

