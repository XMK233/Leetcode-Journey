class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 原作者的思路非常清晰了, 就是哈, 将原来的数组划分为左子树区间和右子树区间.
## 怎么划分呢? (1)右子树空间在左子树空间右边(2)右子树空间里面所有的数都比数组的最后一个数,也就是根节点,要大.
## 所以从左边往右边数, 找到第一个大等于根节点的数, 就是右子树区间的开始, 然后保证右子树区间里面所有的数都大于根节点. 若不满足, 就GG.
## 然后递归判断左子树区间和右子树区间是否满足上述规律.
## 完事儿了. 