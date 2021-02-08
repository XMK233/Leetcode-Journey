'''
[面试题 17.18. 最短超串 - 力扣（LeetCode）](https://leetcode-cn.com/problems/shortest-supersequence-lcci)

假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。

返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。

示例 1:

输入:
big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]
输出: [7,10]

示例 2:

输入:
big = [1,2,3]
small = [4]
输出: []

提示：


	big.length <= 100000
	1 <= small.length <= 100000

'''
import collections
class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        need = collections.Counter(small)
        needCnt = n_s = len(small)
        i = 0
        res = (0, len(big)+1)
        for j,c in enumerate(big):
            if need[c] > 0:
                needCnt -= 1    # 不在t中的字符默认是0，所以大于零的一定是t里的字符
            need[c] -= 1        # 当c出现次数超过所需次数时，need[c]<0，所以needcnt不会小于0
            if needCnt == 0:    # 步骤一：滑动窗口包含了所有T元素
                while True:     # 步骤二：增加i，排除多余元素
                    c = big[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j-i < res[1]-res[0]:   #记录结果
                    res =[i,j]
                    if j - i == n_s:
                        return res
                need[big[i]] += 1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return [] if res[1] > len(big) else res

# 作者：joeylin-m
# 链接：https://leetcode-cn.com/problems/shortest-supersequence-lcci/solution/he-0076zui-xiao-fu-gai-zi-chuan-lei-si-d-naat/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。