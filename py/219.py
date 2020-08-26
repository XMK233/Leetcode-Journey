class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        ## 思路多样，最直接是用哈希。
        ## 如果我用的是这种思路，需要考量的是，如果距离已经明知大于k了，或许就不用更新list了？
        record = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in record:
                for history_index in record[num]:
                    if i - history_index <= k:
                        return True
                record[num].append(i)
            else:
                record[num] = [i]
        return False
        ## 你如果想骚一点，也可以排序然后从第二个开始数，有没有跟前面重复的，有就返回true呗。




s = Solution()
print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))