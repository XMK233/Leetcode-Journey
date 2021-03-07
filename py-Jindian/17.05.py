'''
[面试题 17.05. 字母与数字 - 力扣（LeetCode）](https://leetcode-cn.com/problems/find-longest-subarray-lcci)

给定一个放有字符和数字的数组，找到最长的子数组，且包含的字符和数字的个数相同。

返回该子数组，若存在多个最长子数组，返回左端点最小的。若不存在这样的数组，返回一个空数组。

示例 1:

输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]

输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]


示例 2:

输入: ["A","A"]

输出: []


提示：


	array.length <= 100000

'''

class Solution:
    def findLongestSubarray(self, array):
        diffToStartIndex = {}
        diff = 0
        s, e = 0, -1
        for i, c in enumerate(array):
            if '0' <= c[0] <= '9':
                diff += 1
            else:
                diff -= 1
            if diff == 0 and i > e - s:
                s, e = -1, i
            if diff not in diffToStartIndex:
                diffToStartIndex[diff] = i
            elif i - diffToStartIndex[diff] > e - s:
                s, e = diffToStartIndex[diff], i
        return array[s + 1:e + 1]

print(
    Solution().findLongestSubarray(
        ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
    )
)

# 作者：suibianfahui
# 链接：https://leetcode-cn.com/problems/find-longest-subarray-lcci/solution/chai-zhi-zi-dian-by-suibianfahui/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
