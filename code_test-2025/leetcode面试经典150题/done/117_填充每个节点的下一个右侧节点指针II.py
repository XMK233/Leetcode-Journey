"""
117. 填充每个节点的下一个右侧节点指针 II

给定一个二叉树：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。

初始状态下，所有 next 指针都被设置为 NULL 。

进阶：
- 你只能使用常量级额外空间。
- 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

示例：
输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（通过 next 指针）排列，同一层节点由 next 指针连接，'#' 标识每层的结束。

提示：
- 树中的节点数小于 4096
- -1000 <= node.val <= 1000
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        方法1: 层序遍历（BFS）使用队列
        使用队列进行层序遍历，将同一层的节点连接起来
        
        算法思路：
        1. 使用队列存储当前层的所有节点
        2. 对于每一层，从左到右连接节点
        3. 将下一层的节点加入队列
        
        时间复杂度: O(n) - n为节点总数，每个节点访问一次
        空间复杂度: O(w) - w为树的最大宽度，需要存储一层的节点
        """
        if not root:
            return root
        
        from collections import deque
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            prev_node = None
            
            # 处理当前层的所有节点
            for i in range(level_size):
                current_node = queue.popleft()
                
                # 连接当前节点和前一个节点
                if prev_node:
                    prev_node.next = current_node
                prev_node = current_node
                
                # 将子节点加入队列（下一层）
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            
            # 当前层最后一个节点的next保持为None（默认）
        
        return root
    
    def connect_v2(self, root: 'Node') -> 'Node':
        """
        方法2: 使用已建立的next指针
        利用上一层已经建立的next指针来遍历当前层
        
        算法思路：
        1. 使用dummy节点作为每一层的起始节点
        2. 使用prev指针跟踪当前层的上一个节点
        3. 通过上一层的next指针来遍历当前层
        
        时间复杂度: O(n) - 每个节点访问一次
        空间复杂度: O(1) - 只使用了常数个额外变量
        """
        if not root:
            return root
        
        # 从根节点开始，逐层处理
        current_level_start = root
        
        while current_level_start:
            # dummy节点用于标记下一层的起始位置
            dummy = Node(0)
            prev = dummy
            current = current_level_start
            
            # 遍历当前层的所有节点
            while current:
                # 处理左子节点
                if current.left:
                    prev.next = current.left
                    prev = current.left
                
                # 处理右子节点
                if current.right:
                    prev.next = current.right
                    prev = current.right
                
                # 移动到当前层的下一个节点
                current = current.next
            
            # 移动到下一层
            current_level_start = dummy.next
        
        return root
    
    def connect_v3(self, root: 'Node') -> 'Node':
        """
        方法3: 递归解法（前序遍历）
        使用递归的方式连接节点
        
        算法思路：
        1. 连接当前节点的左右子节点
        2. 递归处理左子树和右子树
        3. 处理跨子树的连接（左子树的最右节点连接右子树的最左节点）
        
        时间复杂度: O(n) - 每个节点访问一次
        空间复杂度: O(h) - h为树的高度，递归栈空间
        """
        if not root:
            return root
        
        def connect_nodes(left_node: 'Node', right_node: 'Node') -> None:
            """连接两个节点及其子节点"""
            if not left_node or not right_node:
                return
            
            # 连接这两个节点
            left_node.next = right_node
            
            # 连接左子节点的左右子树
            connect_nodes(left_node.left, left_node.right)
            
            # 连接右子节点的左右子树
            connect_nodes(right_node.left, right_node.right)
            
            # 连接跨子树的节点
            connect_nodes(left_node.right, right_node.left)
        
        # 从根节点的左右子节点开始
        connect_nodes(root.left, root.right)
        return root
    
    def connect_v4(self, root: 'Node') -> 'Node':
        """
        方法4: 优化的迭代解法（使用哨兵节点）
        结合方法2的优点，使用更简洁的实现
        
        算法思路：
        1. 使用哨兵节点(sentinel)简化边界处理
        2. 使用tail指针跟踪当前层的构建进度
        3. 一层一层地构建next连接
        
        时间复杂度: O(n) - 每个节点访问一次
        空间复杂度: O(1) - 只使用了常数个额外变量
        """
        if not root:
            return root
        
        # 从根节点开始处理
        current = root
        
        while current:
            # 创建哨兵节点，简化下一层的连接操作
            sentinel = Node(0)
            tail = sentinel
            
            # 遍历当前层的所有节点
            node = current
            while node:
                # 处理左子节点
                if node.left:
                    tail.next = node.left
                    tail = tail.next
                
                # 处理右子节点
                if node.right:
                    tail.next = node.right
                    tail = tail.next
                
                # 移动到当前层的下一个节点
                node = node.next
            
            # 移动到下一层
            current = sentinel.next
        
        return root


def create_test_tree() -> Node:
    """创建测试用的二叉树"""
    # 构建树: [1,2,3,4,5,null,7]
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    return root


def create_perfect_tree() -> Node:
    """创建完全二叉树"""
    # 构建完全二叉树: [1,2,3,4,5,6,7]
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root


def print_level_order(root: Node) -> List[List[int]]:
    """按层序打印树，用于验证结果"""
    if not root:
        return []
    
    result = []
    current_level = root
    
    while current_level:
        level_values = []
        node = current_level
        
        # 收集当前层的值
        while node:
            level_values.append(node.val)
            node = node.next
        
        result.append(level_values)
        
        # 移动到下一层
        node = current_level
        next_level_start = None
        while node and not next_level_start:
            if node.left:
                next_level_start = node.left
            elif node.right:
                next_level_start = node.right
            node = node.next
        
        current_level = next_level_start
    
    return result


def test_solution():
    """测试函数"""
    solution = Solution()
    
    print("测试填充每个节点的下一个右侧节点指针 II：")
    print("=" * 60)
    
    # 测试用例1：题目示例
    print("测试用例1：题目示例 [1,2,3,4,5,null,7]")
    root1 = create_test_tree()
    result1 = solution.connect(root1)
    level_order1 = print_level_order(result1)
    print(f"层序遍历结果: {level_order1}")
    print(f"期望: [[1], [2, 3], [4, 5, 7]]")
    print()
    
    # 测试用例2：完全二叉树
    print("测试用例2：完全二叉树 [1,2,3,4,5,6,7]")
    root2 = create_perfect_tree()
    result2 = solution.connect_v2(root2)
    level_order2 = print_level_order(result2)
    print(f"层序遍历结果: {level_order2}")
    print(f"期望: [[1], [2, 3], [4, 5, 6, 7]]")
    print()
    
    # 测试用例3：空树
    print("测试用例3：空树")
    result3 = solution.connect_v3(None)
    print(f"结果: {result3}")
    print(f"期望: None")
    print()
    
    # 测试用例4：单节点
    print("测试用例4：单节点")
    root4 = Node(1)
    result4 = solution.connect_v4(root4)
    level_order4 = print_level_order(result4)
    print(f"层序遍历结果: {level_order4}")
    print(f"期望: [[1]]")
    print()
    
    # 测试所有方法的正确性
    print("验证所有方法的正确性：")
    test_tree = create_test_tree()
    
    methods = [
        ("方法1 (BFS队列)", solution.connect),
        ("方法2 (使用next指针)", solution.connect_v2),
        ("方法3 (递归)", solution.connect_v3),
        ("方法4 (哨兵节点)", solution.connect_v4),
    ]
    
    for method_name, method in methods:
        # 重新创建测试树
        test_root = create_test_tree()
        result = method(test_root)
        level_order = print_level_order(result)
        print(f"{method_name}: {level_order}")


if __name__ == "__main__":
    test_solution()