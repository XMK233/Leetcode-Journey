def sort(lst):
    if (lst is None) or (len(lst) == 0):
        return lst

    for cur_pos in range(len(lst)):
        min_val = lst[cur_pos]
        min_pos = cur_pos
        for j in range(cur_pos, len(lst)):
            if lst[j] < min_val:
                min_val = lst[j]
                min_pos = j
        lst[cur_pos], lst[min_pos] = lst[min_pos], lst[cur_pos]

    return lst

ori_list = [3,4,1,45,6,3,2,3,4]
print(
    sort(ori_list)
)

############################################################################

# 代码中已指定的类名、方法名、参数名，请勿修改，直接返回方法规定的值即可

# Definition for singly-linked list.
#  class ListNode(object):
#      def __init__(self, val=0, next = None):
#          self.val = val
#          self.next = next
class Solution:

    def reverse(self, head):
        lst = []
        while head is not None:
            lst.append(head)
            head = head.next
        lst = lst[::-1]
        for i in range(len(lst) - 1):
            lst[i].next = lst[i + 1]
        lst[-1].next = None
        return lst[0], lst[-1]

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # write your code here.
        new_head = None
        cur_head = head
        last_tail = None
        while cur_head is not None:
            idx = cur_head
            cnt = k - 1
            while (cnt != 0) and (idx is not None):
                idx = idx.next
                cnt -= 1
            ## cur_head: 3 4
            ## idx: 1 6
            if idx is None:
                break
            next_head = idx.next  ## 4 7
            idx.next = None
            rev_part_head, rev_part_tail = self.reverse(cur_head)  ## 3,1; 6,4
            if new_head is None:
                new_head = rev_part_head
            if last_tail is not None:
                last_tail.next = rev_part_head
                last_tail = rev_part_tail
            else:
                last_tail = rev_part_tail

            rev_part_tail.next = next_head  ## 4 7
            cur_head = next_head  ## 4 7
            # if new_head is None:
            #     new_head = rev_part_head
            # if last_tail is None:
            #     last_tail = rev_part_tail
            # last_tail = rev_part_tail

        return new_head if new_head is not None else head

# def print_chain(head):
#     while head is not None:
#         print(head.val)











