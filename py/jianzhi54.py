class Solution:
    def kthLargest(self, root, k):
        def dfs(root):
            if not root: return
            ## go to right branch:
            dfs(root.right)
            if self.k == 0: return
            ## see root itself
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            ## go to left branch
            dfs(root.left)
        ## the k is actually stored in a global variable
        self.k = k
        dfs(root)
        return self.res

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/mian-shi-ti-54-er-cha-sou-suo-shu-de-di-k-da-jie-d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
## 相当于用一个全局变量self.k来存储这个k. k是什么呢? 就是第k大的数嘛.
## 然后就从最大的数开始遍历, 遍历一个, k就减少一个, 直到0, 就说明已经找到第k大的数了.
## 这时直接返回就好, 早停, 不要再往下遍历了.