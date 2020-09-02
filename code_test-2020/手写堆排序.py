## 堆排序有什么功能? 除了排序, 它还可以做诸如, 寻找数组中前/第k大的数字. 
def heapSort(nums):
    def bigHeadHeap(nums, i, length):
        ### 这个函数是仅仅用于调整基本有序的堆.
        ### 什么是基本有序呢? 比如, (1)大顶堆, (2)堆顶元素挪移. 状态2之后, 新的堆顶那个元素不一定是放在了合适
        ### 的位置, 而其他的都放在合适的位置. 这就是所谓基本有序.
        ### 这个函数要做的, 就是把当前堆顶元素给他调到合适的位置.
        ### 所以, i就是目前要调的子树所代表的堆的堆顶. 然后我们每一次都先将左子节点视为目标节点.
        ### 然后寻找左右两个节点里面哪个更大, 如果右节点更大, 我们就视右节点为目标节点.
        target = 2 * i + 1
        while target < length:
            if target + 1 < length and nums[target] < nums[target+1]:
                target += 1
            if nums[target] > nums[i]:
                nums[i], nums[target] = nums[target], nums[i]
                i = target
            ## 更新一下target值
            target = 2 * target + 1
        return
    ## 第一步先弄啥类? 先构造一个初始大顶堆.
    ## 最开始, 要从最后一个非叶节点开始, 调每一个非叶子节点. 最后一个非叶子节点的位置是len//2-1
    for i in range(len(nums) // 2 - 1, -1, -1):
        bigHeadHeap(nums, i, len(nums))
    ## 第二步, 反复地调
    for length in range(len(nums) - 1, -1, -1):
        nums[0], nums[length] = nums[length], nums[0] ## 将堆顶元素和未排序部分的最后一个元素对调.
        bigHeadHeap(nums, 0, length) ## 最后一个元素不考虑了, 把要考虑的元素重新调整一下.
    return

array = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
heapSort(array)
print(array)