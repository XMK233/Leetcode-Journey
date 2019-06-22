/* 83. Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
*
*
* Solutions:
* Nothing particular.
*
* */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
class Solution {
    public ListNode deleteDuplicates(ListNode head) {

        if (head == null){
            return null;
        }

        if (head.next == null){
            return head;
        }

        ListNode p = head;
        for (;p.next != null;){
            if (p.val == p.next.val){
                p.next = p.next.next;
            }
            else{
                p = p.next;
            }
        }

        return head;
    }
}
public class firstTest{
    public static void main(String[] args){
        Solution s = new Solution();
    }
}
