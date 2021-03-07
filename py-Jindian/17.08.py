'''
[面试题 17.08. 马戏团人塔 - 力扣（LeetCode）](https://leetcode-cn.com/problems/circus-tower-lcci)

有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。

示例：

输入：height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
输出：6
解释：从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)

提示：


	height.length == weight.length <= 10000

'''
'''
大概的思路是酱紫的. 
首先, 你要想到两重排序对不对. 第一重是按照身高来升序排序, 然后在此基础上按照体重来降序排序. 
注意哦, 体重是按照降序来排序的. 
然后, 因为身高已经是升序的了, 所以我们只关注体重就好了. 
现在的体重是不单调的. 我们只需要找到体重的序列里面, 最长单调递增的长度就好了. 乌拉. 

参考的思路可以说是OK了, 就是实现的细节还没撸通. 
'''
class Solution:
    def bestSeqAtIndex(self, height, weight) -> int:
        peoples = []
        for i in range(len(height)):
            peoples.append((height[i], weight[i]))

        peoples.sort(key=lambda x: [x[0], -x[1]])
        nums = [w[1] for w in peoples]

        dp = []
        for i in range(len(nums)):
            if not dp or nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                l = 0
                r = len(dp)

                while l < r:
                    mid = (l + r) // 2
                    if dp[mid] == nums[i]:
                        l = mid
                        r = mid
                    elif dp[mid] > nums[i]:
                        r = mid
                    else:
                        l = mid + 1

                dp[l] = nums[i]

        return len(dp)

print(
    Solution().bestSeqAtIndex(
        [3,2,2,3,1,6], [7,3,5,6,2,10]
    )
)

# 作者：godwriter
# 链接：https: // leetcode - cn.com / problems / circus - tower - lcci / solution / pythonzhi - nan - shen - mei - de - dong - tai - gui - hua - shi - x - 4 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。