'''
[剑指 Offer 40. 最小的k个数 - 力扣（LeetCode）](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof)

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]


示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

 

限制：


	0 <= k <= arr.length <= 10000
	0 <= arr[i] <= 10000

'''

import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heapq.heapify(arr)
        return heapq.nsmallest(k, arr)

# 作者：06ykmqqtt
# 链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/shi-yong-heapqqiu-jie-by-06ykmqqtt/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 道理很明显了, 就是用堆排序即可.
## 堆排序有一个特点, 就是第k次堆排序, 就能得到第k小的数字. 比如第一次排序, 就知道最小的数字是多少了.
## 那弄k次, 不就把前k个数字都弄来了嘛.
## 而且python有内置的实现, 岂不美哉?

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