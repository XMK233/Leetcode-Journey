# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/e8a1b01a2df14cb2b228b30ee6a92163?tpId=117&&tqId=37770&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

投票法, 然后再遍历一遍确认.
金典17.10
'''
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        nums = numbers
        if len(nums) == 0:
            return -1
        #####
        curNum = None
        curCnt = 0
        for num in nums:
            if curCnt == 0:
                curNum = num
                curCnt += 1
            else:
                if curNum != num:
                    curCnt -= 1
                    if curCnt == 0:
                        ## 第一次提交的时候
                        curNum = None
                else:
                    curCnt += 1
        if curCnt == 0:
            return 0
        ## 第二次修改, 增加了以下的判断.
        ## 你其实可以知道, 上面的流程走过后, curNum未必是出现次数最多的.
        ## 所以再增加一个遍历的阶段, 如果curNum统计的出现次数确实过半, 才说明这个数是主要元素.
        count = 0
        for num in nums:
            if num == curNum: count += 1
            if count > len(nums)/2:
                return curNum
        return 0