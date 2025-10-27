'''给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

 

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
示例 3：

输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
'''

# 解法：从后往前的双指针方法
# 思路：由于nums1的末尾有足够空间，我们可以从两个数组的末尾开始比较，将较大的元素放到nums1的末尾
# 这样可以避免额外的空间复杂度，并且不会覆盖nums1中尚未处理的元素

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # 初始化三个指针
    # p1指向nums1的最后一个有效元素
    # p2指向nums2的最后一个元素
    # p指向nums1的最后一个位置（用于放置合并后的元素）
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    # 当两个数组都有元素时，进行比较和合并
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # 如果nums2还有剩余元素，需要将它们复制到nums1中
    # 注意：如果nums1有剩余元素，它们已经在正确的位置上了，不需要处理
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# 测试用例
if __name__ == "__main__":
    # 测试用例1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(f"测试用例1结果: {nums1}")  # 预期输出: [1, 2, 2, 3, 5, 6]
    
    # 测试用例2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    print(f"测试用例2结果: {nums1}")  # 预期输出: [1]
    
    # 测试用例3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(f"测试用例3结果: {nums1}")  # 预期输出: [1]