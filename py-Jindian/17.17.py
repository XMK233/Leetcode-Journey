'''
[面试题 17.17. 多次搜索 - 力扣（LeetCode）](https://leetcode-cn.com/problems/multi-search-lcci)

给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，根据smalls中的每一个较短字符串，对big进行搜索。输出smalls中的字符串在big里出现的所有位置positions，其中positions[i]为smalls[i]出现的所有位置。

示例：

输入：
big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]
输出： [[1,4],[8],[],[3],[1,4,7,10],[5]]


提示：


	0 <= len(big) <= 1000
	0 <= len(smalls[i]) <= 1000
	smalls的总字符数不会超过 100000。
	你可以认为smalls中没有重复字符串。
	所有出现的字符均为英文小写字母。

'''
class Solution:
    def multiSearch(self, big, smalls): ## 暴力解法. 没有技术含量.
        res = [[] for small in smalls]
        for i, c in enumerate(big):
            for j, small in enumerate(smalls):
                if small == "":
                    continue
                endIdx = i + len(small)
                if endIdx > len(big):
                    continue
                if big[i:endIdx] == small:
                    res[j].append(i)
        return res

## 暴力解法可以做, 但是效果有限. 考虑用树来弄?
## 可以参考 https://leetcode-cn.com/problems/multi-search-lcci/solution/python-zi-dian-shu-by-wiking-e/

s = Solution().multiSearch(
    "mississippi",
    ["is","ppi","hi","sis","i","ssippi"]
    )
print(s)


