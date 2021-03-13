'''
题目描述
有一种将字母编码成数字的方式：'a'->1, 'b->2', ... , 'z->26'。

现在给一串数字，返回有多少种可能的译码结果
示例1
输入
复制
"12"
返回值
复制
2
说明
2种可能的译码结果（”ab” 或”l”）
示例2
输入
复制
"31717126241541717"
11717126241541717
1?               1
返回值
复制
192
说明
192种可能的译码结果

很简单. 用普通dp算法即可.
但是要注意一些情况, 见代码里的字符串.
'''
#
# 解码
# @param nums string字符串 数字串
# @return int整型
#
class Solution:
    def solve(self , nums ):
        # write code here
        if not nums:
            return 0
        if nums[0] == "0": return 0 ## 如果起始的字符就是0,那直接GG了.
        dp = [0 for i in range(len(nums) + 1)]
        dp[0] = 1
        dp[-1] = 1
        for i in range(1, len(nums)):
            curInt = int(nums[i - 1] + nums[i]) ## 看看这个小段是不是一个1~26之间的数字.
            if nums[i] == "0" and nums[i - 1] != "0": ## 当前字符是0,前一个字符不是0, 比如10, 20酱紫的组合
                if curInt >= 1 and curInt <= 26: ## 能够找到对应字母就好办
                    dp[i] = dp[i - 2]
                else: ## 找不到,就无法编译成字符串哦. 比如30, 那这一颗老鼠屎是坏了一锅粥的.
                    return 0
            elif nums[i] != "0" and nums[i - 1] == "0": ## 当前字符不是0,前一个字符是0. 比如01的组合, 1绝对无法与前面的0组合成字符串的嘛.
                dp[i] = dp[i - 1]
            elif nums[i] != "0" and nums[i - 1] != "0": ## 当前字符与前一个字符均不是0. 这就是最普通的情况了.
                if curInt >= 1 and curInt <= 26: ## 能够找到对应字母
                    dp[i] = dp[i - 1] + dp[i - 2]
                else: ## 不能找到对应的字母
                    dp[i] = dp[i-1]
            else: ## 当前字符与前一个字符均是0, 比如出现了00这样的组合, 那也是直接GG的.
                return 0
        return dp[-2]

print(Solution().solve("10"))
