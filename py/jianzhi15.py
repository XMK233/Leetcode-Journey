class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/mian-shi-ti-15-er-jin-zhi-zhong-1de-ge-shu-wei-yun/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 这种方法的原理是什么呢？就是，n与1相与，就知道最后一位是不是1；然后每与一次，n就右移一位，直到n移到0为止。
## 了事。

## 当然，更好的技巧是什么呢？
## 每一次n与上n-1，就能将n的最后一个1翻转为0. 所以在n全部被翻转为0之前，这样的与操作能进行几次，就有几个1.