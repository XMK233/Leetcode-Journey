'''简单
相关标签
premium lock icon
相关企业
提示
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
 

示例 1：

输入：s = "()"

输出：true

示例 2：

输入：s = "()[]{}"

输出：true

示例 3：

输入：s = "(]"

输出：false

示例 4：

输入：s = "([])"

输出：true

示例 5：

输入：s = "([)]"

输出：false

 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成'''

class Solution:
    def isValid(self, s: str) -> bool:
        """
        判断括号字符串是否有效
        解题思路：使用栈（后进先出）数据结构
        时间复杂度：O(n)，其中n是字符串长度
        空间复杂度：O(n)，最坏情况下需要存储所有左括号
        """
        # 特殊情况处理：如果字符串长度为奇数，直接返回False
        if len(s) % 2 != 0:
            return False
        
        # 创建括号映射字典，用于快速查找匹配的左括号
        # 键为右括号，值为对应的左括号
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        # 初始化一个空栈，用于存储左括号
        stack = []
        
        # 遍历字符串中的每个字符
        for char in s:
            # 如果是右括号
            if char in bracket_map:
                # 检查栈是否为空，如果为空说明没有匹配的左括号
                # 或者检查栈顶元素是否与当前右括号匹配
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:
                # 如果是左括号，将其入栈
                stack.append(char)
        
        # 最后检查栈是否为空
        # 如果为空说明所有括号都匹配，返回True
        # 否则说明有未匹配的左括号，返回False
        return not stack

# 测试用例
if __name__ == "__main__":
    solution = Solution()
    
    # 示例1
    s1 = "()"
    result1 = solution.isValid(s1)
    print(f"示例1: s = '{s1}'")
    print(f"输出: {result1}")
    print(f"预期: True")
    print()
    
    # 示例2
    s2 = "()[]{}"
    result2 = solution.isValid(s2)
    print(f"示例2: s = '{s2}'")
    print(f"输出: {result2}")
    print(f"预期: True")
    print()
    
    # 示例3
    s3 = "(]"
    result3 = solution.isValid(s3)
    print(f"示例3: s = '{s3}'")
    print(f"输出: {result3}")
    print(f"预期: False")
    print()
    
    # 示例4
    s4 = "([])"
    result4 = solution.isValid(s4)
    print(f"示例4: s = '{s4}'")
    print(f"输出: {result4}")
    print(f"预期: True")
    print()
    
    # 示例5
    s5 = "([)]"
    result5 = solution.isValid(s5)
    print(f"示例5: s = '{s5}'")
    print(f"输出: {result5}")
    print(f"预期: False")
    print()
    
    # 边界测试用例
    s6 = "{[]}"
    result6 = solution.isValid(s6)
    print(f"边界测试: s = '{s6}'")
    print(f"输出: {result6}")
    print(f"预期: True")