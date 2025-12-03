from typing import List
from collections import deque

'''
基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。

假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 bank 中）

给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。

注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。

 

示例 1：

输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
输出：1
示例 2：

输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
输出：2
示例 3：

输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
输出：3
 

提示：

start.length == 8
end.length == 8
0 <= bank.length <= 10
bank[i].length == 8
start、end 和 bank[i] 仅由字符 ['A', 'C', 'G', 'T'] 组成
'''
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """找出从startGene变化为endGene所需的最少变化次数
        
        Args:
            startGene: 起始基因序列
            endGene: 目标基因序列
            bank: 有效的基因库，只有基因库中的基因才是有效的基因序列
            
        Returns:
            int: 能够使startGene变化为endGene所需的最少变化次数，如果无法完成则返回-1
        """
        # 边界情况检查
        if startGene == endGene:
            return 0
        
        # 将bank转换为集合，方便快速查找
        bank_set = set(bank)
        
        # 如果目标基因不在基因库中，无法完成变化
        if endGene not in bank_set:
            return -1
        
        # 定义基因中可能的字符
        chars = ['A', 'C', 'G', 'T']
        
        # 使用队列进行BFS，队列中的元素为(当前基因序列, 当前变化次数)
        queue = deque([(startGene, 0)])
        
        # 记录已经访问过的基因，避免重复访问
        visited = set([startGene])
        
        # BFS搜索
        while queue:
            current, steps = queue.popleft()
            
            # 遍历当前基因的每一个位置
            for i in range(len(current)):
                # 尝试将当前位置替换为其他字符
                for char in chars:
                    # 跳过与当前字符相同的替换
                    if char == current[i]:
                        continue
                    
                    # 生成新的基因序列
                    new_gene = current[:i] + char + current[i+1:]
                    
                    # 如果新的基因序列是目标基因
                    if new_gene == endGene:
                        return steps + 1
                    
                    # 如果新的基因序列在基因库中且未被访问过
                    if new_gene in bank_set and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, steps + 1))
        
        # 如果无法到达目标基因
        return -1


# 测试用例
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1：示例1
    start1 = "AACCGGTT"
    end1 = "AACCGGTA"
    bank1 = ["AACCGGTA"]
    print(f"测试用例1结果: {solution.minMutation(start1, end1, bank1)}")  # 预期输出: 1
    
    # 测试用例2：示例2
    start2 = "AACCGGTT"
    end2 = "AAACGGTA"
    bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(f"测试用例2结果: {solution.minMutation(start2, end2, bank2)}")  # 预期输出: 2
    
    # 测试用例3：示例3
    start3 = "AAAAACCC"
    end3 = "AACCCCCC"
    bank3 = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    print(f"测试用例3结果: {solution.minMutation(start3, end3, bank3)}")  # 预期输出: 3
    
    # 测试用例4：目标基因不在基因库中
    start4 = "AACCGGTT"
    end4 = "AACCGGTC"
    bank4 = ["AACCGGTA", "AACCGCTA"]
    print(f"测试用例4结果: {solution.minMutation(start4, end4, bank4)}")  # 预期输出: -1
    
    # 测试用例5：起始基因等于目标基因
    start5 = "AACCGGTT"
    end5 = "AACCGGTT"
    bank5 = ["AACCGGTA", "AACCGCTA"]
    print(f"测试用例5结果: {solution.minMutation(start5, end5, bank5)}")  # 预期输出: 0
        