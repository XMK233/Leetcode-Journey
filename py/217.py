class Solution:
    def containsDuplicate(self, nums) -> bool:
        ## 思路多样，最直接是用哈希。
        record = {}
        for num in nums:
            if num in record:
                return True
            else:
                record[num] = "1"
        return False
        ## 你如果想骚一点，也可以排序然后从第二个开始数，有没有跟前面重复的，有就返回true呗。




s = Solution()
print(s.containsDuplicate([1, 2, 3, 4, 1, 6]))