"""
97. 交错字符串

给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1

交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接。

示例 1:
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
解释：
s1 = "aa" + "bc" + "c"
s2 = "dbbc" + "a"
s3 = "aadbbcbcac"

示例 2:
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false

示例 3:
输入：s1 = "", s2 = "", s3 = ""
输出：true

提示：
- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1、s2、和 s3 都由小写英文字母组成
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        方法1: 动态规划
        使用二维DP数组来记录s1的前i个字符和s2的前j个字符是否能组成s3的前i+j个字符
        
        算法思路：
        1. dp[i][j] 表示 s1[:i] 和 s2[:j] 是否能组成 s3[:i+j]
        2. 状态转移：
           - 如果 s1[i-1] == s3[i+j-1]，则 dp[i][j] = dp[i-1][j]
           - 如果 s2[j-1] == s3[i+j-1]，则 dp[i][j] = dp[i][j-1]
           - 两者满足其一即可
        
        时间复杂度: O(m*n) - m和n分别是s1和s2的长度
        空间复杂度: O(m*n) - 需要二维DP数组
        """
        m, n, l = len(s1), len(s2), len(s3)
        
        # 长度检查
        if m + n != l:
            return False
        
        # 创建DP数组
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # 空字符串可以组成空字符串
        
        # 初始化第一行（只使用s2）
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        # 初始化第一列（只使用s1）
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        # 填充DP数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 检查s1的当前字符是否匹配
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                
                # 检查s2的当前字符是否匹配
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        
        return dp[m][n]
    
    def isInterleave_v2(self, s1: str, s2: str, s3: str) -> bool:
        """
        方法2: 动态规划 + 空间优化
        使用一维数组优化空间复杂度
        
        算法思路：
        由于dp[i][j]只依赖于dp[i-1][j]和dp[i][j-1]，可以用一维数组优化
        
        时间复杂度: O(m*n)
        空间复杂度: O(n) - 只需要一维数组
        """
        m, n, l = len(s1), len(s2), len(s3)
        
        if m + n != l:
            return False
        
        # 确保s2是较短的字符串，减少空间使用
        if n > m:
            return self.isInterleave_v2(s2, s1, s3)
        
        # 一维DP数组
        dp = [False] * (n + 1)
        dp[0] = True
        
        # 初始化第一行
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        
        # 填充DP数组
        for i in range(1, m + 1):
            # 更新第一列
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            
            # 更新其他列
            for j in range(1, n + 1):
                # 注意：这里需要从上次的dp[j]（相当于dp[i-1][j]）和dp[j-1]（相当于dp[i][j-1]）更新
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[n]
    
    def isInterleave_v3(self, s1: str, s2: str, s3: str) -> bool:
        """
        方法3: 深度优先搜索（DFS）+ 记忆化
        使用递归和记忆化来避免重复计算
        
        算法思路：
        从s3的末尾开始匹配，递归检查两种可能：
        1. s3的最后一个字符来自s1
        2. s3的最后一个字符来自s2
        
        时间复杂度: O(m*n) - 每个状态只计算一次
        空间复杂度: O(m*n) - 记忆化数组和递归栈
        """
        m, n, l = len(s1), len(s2), len(s3)
        
        if m + n != l:
            return False
        
        # 记忆化数组
        memo = {}
        
        def dfs(i: int, j: int) -> bool:
            # 基本情况：两个字符串都匹配完了
            if i == m and j == n:
                return True
            
            # 检查记忆化
            if (i, j) in memo:
                return memo[(i, j)]
            
            result = False
            
            # 尝试从s1匹配
            if i < m and s1[i] == s3[i + j]:
                result = result or dfs(i + 1, j)
            
            # 尝试从s2匹配
            if j < n and s2[j] == s3[i + j]:
                result = result or dfs(i, j + 1)
            
            # 记忆化结果
            memo[(i, j)] = result
            return result
        
        return dfs(0, 0)
    
    def isInterleave_v4(self, s1: str, s2: str, s3: str) -> bool:
        """
        方法4: 广度优先搜索（BFS）
        使用BFS遍历所有可能的匹配路径
        
        算法思路：
        1. 使用队列存储当前在s1和s2中的位置
        2. 使用集合记录访问过的状态，避免重复
        3. 从队列中取出状态，尝试两种匹配方式
        
        时间复杂度: O(m*n) - 每个状态只访问一次
        空间复杂度: O(m*n) - 队列和访问集合
        """
        m, n, l = len(s1), len(s2), len(s3)
        
        if m + n != l:
            return False
        
        from collections import deque
        queue = deque([(0, 0)])
        visited = set()
        visited.add((0, 0))
        
        while queue:
            i, j = queue.popleft()
            
            # 如果两个字符串都匹配完了
            if i == m and j == n:
                return True
            
            # 尝试从s1匹配
            if i < m and s1[i] == s3[i + j] and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                queue.append((i + 1, j))
            
            # 尝试从s2匹配
            if j < n and s2[j] == s3[i + j] and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                queue.append((i, j + 1))
        
        return False


def test_solution():
    """测试函数"""
    solution = Solution()
    
    # 测试用例
    test_cases = [
        ("aabcc", "dbbca", "aadbbcbcac", True),    # 基本测试 - 交错成功
        ("aabcc", "dbbca", "aadbbbaccc", False),   # 基本测试 - 交错失败
        ("", "", "", True),                        # 空字符串
        ("a", "", "a", True),                     # 一个空字符串
        ("", "a", "a", True),                     # 另一个空字符串
        ("abc", "def", "adbcef", True),           # 简单交错
        ("abc", "def", "abdecf", False),          # 无法交错
        ("aa", "ab", "aaab", True),               # 重复字符
        ("aa", "ab", "aaba", True),               # 另一种交错方式
        ("aaaaaaaa", "aaaaaaaa", "aaaaaaaaaaaaaaaa", True),  # 长字符串
        ("ab", "bc", "babc", True),               # 边界情况
        ("ab", "bc", "abcb", False),              # 无法交错
    ]
    
    print("测试交错字符串问题：")
    print("=" * 60)
    
    for i, (s1, s2, s3, expected) in enumerate(test_cases, 1):
        result1 = solution.isInterleave(s1, s2, s3)
        result2 = solution.isInterleave_v2(s1, s2, s3)
        result3 = solution.isInterleave_v3(s1, s2, s3)
        result4 = solution.isInterleave_v4(s1, s2, s3)
        
        print(f"测试用例 {i}:")
        print(f"s1 = '{s1}', s2 = '{s2}', s3 = '{s3}'")
        print(f"期望结果: {expected}")
        print(f"方法1结果: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"方法2结果: {result2} {'✓' if result2 == expected else '✗'}")
        print(f"方法3结果: {result3} {'✓' if result3 == expected else '✗'}")
        print(f"方法4结果: {result4} {'✓' if result4 == expected else '✗'}")
        print("-" * 40)


if __name__ == "__main__":
    test_solution()