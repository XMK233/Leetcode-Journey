class Solution:
    def isStraight(self, nums) -> bool:
        numbers = nums
        # write code here
        if not numbers:
            return False
        zeros, maxi, mini = 0, -1, 14
        counts = 0
        exist = set()
        for num in numbers:
            if num == 0:
                zeros += 1
                continue
            if num in exist:
                return False
            if num > maxi:
                maxi = num
            if num < mini:
                mini = num
            counts += 1
            exist.add(num)
        return maxi - mini + 1 - counts <= zeros

## https://blog.csdn.net/qq_27668313/article/details/103111258
## "统计数组中最大值和最小值，0的个数和非0数字的个数。如果最大值和最小值之间的空位可以被0和剩余非0数字填满，则数组是连续的，否则不连续。"