class Solution:
    def restoreIpAddresses(self , s: str):
        # write code here
        ## 用回溯算法，dfs。
        ## TODO: consider the special cases
        res = []
        path = []
        def dfs(string, level):
            '''
            :param string: the string to be converted to IP address
            :param level: the level number left
            :return: list of string
            '''
            if len(string) < level or len(string) > (level * 3):
                return
            if len(string) == 0 and level == 0:
                res.append(".".join(path))
                return
            for i in range(1, min(len(string), 3) + 1):
                cur_level = string[:i]
                if cur_level[0] == "0" and len(cur_level) > 1:
                    ## I didn't considered leading 0 problem.
                    break
                cur_level_int = int(cur_level)
                if cur_level_int < 0 or cur_level_int > 255:
                    break
                path.append(cur_level)
                dfs(string[i:], level - 1)
                path.pop(-1)

        dfs(s, 4)
        return res

print(Solution().restoreIpAddresses("010010"))

'''
描述
现在有一个只包含数字的字符串，将该字符串转化成IP地址的形式，返回所有可能的情况。
例如：
给出的字符串为"25525522135",
返回["255.255.22.135", "255.255.221.35"]. (顺序没有关系)

数据范围：字符串长度 0 \le n \le 120≤n≤12
要求：空间复杂度 O(n!)O(n!),时间复杂度 O(n!)O(n!)

注意：ip地址是由四段数字组成的数字序列，格式如 "x.x.x.x"，其中 x 的范围应当是 [0,255]。

示例1
输入：
"25525522135"
复制
返回值：
["255.255.22.135","255.255.221.35"]
复制
示例2
输入：
"1111"
复制
返回值：
["1.1.1.1"]
复制
示例3
输入：
"000256"
复制
返回值：
"[]"
'''