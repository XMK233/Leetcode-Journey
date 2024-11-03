#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def findPeakElement(self , nums: list[int]) -> int:
        # write code here
        '''
        思路是啥呢？看了一些题解，有了一些思路。
        就是说，用二分查找的方式，一开始从数组两端的【0】和【len-1】找到一个mid点。
        如果mid点比右边的大，说明有可能mid就是一个峰值点。那么就在left和mid之间找峰值点。
        如果mid点比右边的小，说明mid肯定不是一个峰值点。那么就去[mid+1]和right之间寻找峰值点。
        一直找，直到left和right碰到一起。
        :param nums:
        :return:
        '''
        left, right = 0, len(nums)-1
        while left != right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            elif nums[mid] < nums[mid+1]:
                left = mid+1
        return left


print(Solution().findPeakElement(
[1,2,3,1]

))