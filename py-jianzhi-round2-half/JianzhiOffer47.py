class Solution:
    def permuteUnique(self, nums):
        ## 如果只包含一个元素, 那就原样返回即可.
        if len(nums) == 1:
            return [nums]
        ## 如果包含不止一个元素, 那就得费点功夫.
        nums.sort()
        lastVal = nums[0] - 1 ## 这是干什么呢? 这个值表示, 这个值比最小的数字还要小一点.
        heheda = []
        for i in range(0, len(nums)):
            ## 如果碰到一样的值, 就跳过
            if nums[i] == lastVal:
                continue
            ## 碰到不一样的值, 才继续处理
            else:
                lastVal = nums[i]
            ###############
            if i == 0:
                otherPart = nums[1:]
            elif i == len(nums) - 1:
                otherPart = nums[0:-1]
            else:
                headPartList = nums[0:i]
                tailPartList = nums[i + 1:]
                otherPart = headPartList + tailPartList

            for l in self.permuteUnique(otherPart):
                l_new = [nums[i]] + l
                # if l_new not in heheda:
                #     heheda.append(l_new)
                heheda.append(l_new)
        return heheda


s = Solution()
print(s.permuteUnique([1,1,2]))