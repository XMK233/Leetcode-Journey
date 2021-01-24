'''
[剑指 Offer 09. 用两个栈实现队列 - 力扣（LeetCode）](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof)

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]


示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]


提示：


	1 <= values <= 10000
	最多会对 appendTail、deleteHead 进行 10000 次调用

'''
'''
//作者：jyd
//        链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/solution/mian-shi-ti-09-yong-liang-ge-zhan-shi-xian-dui-l-2/
//        来源：力扣（LeetCode）
//        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

/*
* 道理很简单.
* push的话永远往A里面推.
* 只要B非空, 那么就从B弹出.
* 如果B空了, A非空, 那么就要把A里面的东西给一次性全部灌进B中, 然后再从B中弹出.
* 如果AB皆空, 那就返回-1, 也就是出错了. 
* */
'''
class CQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def appendTail(self, value: int) -> None:
        self.stackA.append(value)


    def deleteHead(self) -> int:
        if len(self.stackB) > 0:
            return self.stackB.pop(-1)
        elif len(self.stackA) > 0:
            while len(self.stackA) > 0:
                self.stackB.append(
                    self.stackA.pop(-1)
                )
            ## 这里当年写错了. 最后一定要记得返回哦.
            return self.stackB.pop(-1)
        return -1

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