# https://www.jianshu.com/p/960cf375c40a
## 从字符串的角度来判断两数大小. 这是个技巧. 也是根本.
## 然后, 利用上述的大小判断方法, 根据从大到小的顺序对原数组进行排序. 排序的方法就多样了. 可以用快排啊酱紫的, 让排序更快. 下面的方法比较慢的.
## 这种思路好.
## 我想了半天的暴力破解的方法: 按位来比较, 然后把某一位相等的数字放在一个桶里, 对每一个桶进行递归, 然后把每一个桶的结果合并起来.

class Solution:
    def smaller(self,a,b):
        strA = str(a) + str(b)
        strB = str(b) + str(a)
        if strA > strB :
            return False
        else:
            return True

    def largestNumber(self, nums):
        resultStr = ""
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if self.smaller(nums[i],nums[j]):
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        for i in nums:
            resultStr = resultStr + str(i)
        if (resultStr[0]=='0'):
            return '0'
        return resultStr