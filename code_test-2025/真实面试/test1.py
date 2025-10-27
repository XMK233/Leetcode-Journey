## 题目大概是怎么样的呢？
## 一个数组，它代表了一栋大楼的楼层。然后呢数组的值呢表明从这个楼层往上或者往下能跳几层。
## 不能跳到地下或者超出楼层。
## 然后我给定一个起始位置和一个结束位置，问我最少跳几步可以跳到目标楼层。

## 你是怎么学习算法的？我说什么学习书本网络，然后实践操作。我其实还应该答我经常看论文学习。哎呀当时没想到看论文，因为论文是更新最快的。
## 关于从风控跳转到推荐，是怎么看的？他这个问题语焉不详。
# 我就说基于一些风险的经验的迁移，然后这个业务背景我喜欢且比较熟悉，符合我的期待并且和我的经验相差不愿，可以自学，跟同事学习，然后确定业务目标然后优化。
# 我说我是对技术有热情的。但是当时答的时候没有很好地把这份热情展现出来。我完全可以补充说，我看了很多本书，nlp，cv，多模态，图计算，大模型，推荐系统。
# 谦虚地说，我不能说我对某一领域钻研很深，但至少要是咱们能够结合业务谈谈怎么使用算法，我基本都能说个所以然，不会一脸懵逼，我在刚才说的项目里面用nlp，虽然探索有一定曲折，但在算法这一块总体是不懵逼的，
# 不至于因为风控领域只用树模型或者lr，就对深度学习或者其他东西一无所知。
# 不过我觉得还可以说：我如果能够从事一份推荐的岗位的话，最好的学习不是学习书本，而是快速地熟悉公司现有的整套体系，找一个同事的项目从头研读，比如花一周的实践，
# 从业务目标，到算法实现，到部署上线，再到监控优化的全过程，
# 从中学习到咱们这边工作的共性，以及针对单个项目中可以个性化的部分。


class TreeNode:
    def __init__(self, x, y):
        self.val = x
        self.pos = y
        self.left = None
        self.right = None


def build_tree(val_list, cur_pos):
    cur_val = val_list[cur_pos]
    if cur_val == -1: ## 如果已经标记过，就返回-1.
        return None
    left_pos = cur_pos - cur_val
    right_pos = cur_pos + cur_val

    cur_node = TreeNode(cur_val, cur_pos)
    if left_pos < 0:
        cur_node.left = None
    else:
        val_list[cur_pos] = -1
        cur_node.left = build_tree(val_list, left_pos)

    if right_pos >= len(val_list):
        cur_node.right = None
    else:
        val_list[cur_pos] = -1
        cur_node.right = build_tree(val_list, right_pos)

    return cur_node

def find_shallowest_level(tree_node, target_pos):
    if tree_node is None:
        return float("inf")
    elif tree_node.pos == target_pos:
        return 0
    else:
        left_levels = find_shallowest_level(tree_node.left, target_pos)
        right_levels = find_shallowest_level(tree_node.right, target_pos)
        return 1+min(left_levels, right_levels)


val_list = [1,3,2,1,1]

tree = build_tree(val_list, 1)

print(find_shallowest_level(tree, 3))


print("stop")