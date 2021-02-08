'''
[面试题 17.19. 消失的两个数字 - 力扣（LeetCode）](https://leetcode-cn.com/problems/missing-two-lcci)

给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？

以任意顺序返回这两个数字均可。

示例 1:

输入: [1]
输出: [2,3]

示例 2:

输入: [2,3]
输出: [1,4]

提示：


	nums.length <= 30000

'''

class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        # 方法1 : cyclic sort
        ret = []
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            # 因为缺两个，就只拍从1到n的，n+1与n+2 补位给缺失的元素
            if j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i+1:
                ret.append(i+1)
        if len(ret) == 1:
            # 这里怎么处理？
            # 上面找到的都是[1...n]的，所以缺的可能性有两种 n + 1 或者 n + 2
            if n + 1 in nums:
                ret.append(n+2)
            else:
                ret.append(n+1)
        elif len(ret) == 0:
            return [n+1, n+2]
        return ret

# 作者：cui-jin-hao-_official
# 链接：https://leetcode-cn.com/problems/missing-two-lcci/solution/python-quan-pai-xu-fen-zu-yi-huo-by-cui-jin-hao-_o/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
