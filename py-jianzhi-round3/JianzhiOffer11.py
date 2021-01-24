'''
[剑指 Offer 11. 旋转数组的最小数字 - 力扣（LeetCode）](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof)

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1


示例 2：

输入：[2,2,2,0,1]
输出：0


注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
'''
'''
/*没有完全弄出来.
mid, mid+1这两个地方参考了答案.
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
else里面也是参考了的. 这种情况就是numbers[mid] < numbers[tail], 没法判断, 那就把tail往回缩一格, 重新判断.
但是其他的地方基本是自己想出来并实现的. 并且程序的大致结构上已经和参考答案别无二致了.
*/

这道题总的来说思路是二分法查找. 
最重要的, 是对比数组中位, 中位要么大于数组尾部值, 要么小于. 两种情况, 你都可以做一些二分查找的区间移动的事情. 
'''
class Solution:
    def minArray(self, numbers) -> int:
        head = 0
        tail = len(numbers) - 1
        while head < tail:
            ## 如果头小于尾, 那就是一个有序数组, 那么头必定是最小的.
            if numbers[head] < numbers[tail]:
                return numbers[head]
            mid = (tail - head) // 2 + head
            if numbers[mid] > numbers[tail]:
                head = mid + 1
            elif numbers[mid] < numbers[tail]:
                tail = mid
            else:
                tail -= 1
        return numbers[head]




##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()