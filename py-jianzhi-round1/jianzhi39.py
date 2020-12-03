class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/mian-shi-ti-39-shu-zu-zhong-chu-xian-ci-shu-chao-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 除了你能想到的两种方法, 参考的这种更好.
## 利用的原理是, 假定当前的数字就是所谓众数, 那么它会被用作抵消其他的数字, 如果真是众数, 那么遍历完一遍之后, 它不会被抵消完.