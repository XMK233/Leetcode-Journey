public class Jianzhi52 {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // 基本的原理: 让长的链表先走一段路程, 然后再一起走, 走到重合的点即可.
        ListNode pA = headA, pB = headB;
        int lengthA = 0, lengthB = 0;
        for (;pA != null;pA = pA.next){
            lengthA++;
        }
        for (;pB != null;pB = pB.next){
            lengthB++;
        }
        if (lengthA > lengthB){
            int deltaLength = lengthA - lengthB;
            pA = headA; pB = headB;
            for (; pA != null & pB != null; ){
                if (deltaLength > 0) {
                    pA = pA.next;
                    deltaLength--;
                }
                else{
                    if (pA == pB)
                        return pA;
                    pA = pA.next;
                    pB = pB.next;
                }
            }
        }
        else{
            int deltaLength = lengthB - lengthA;
            pA = headA; pB = headB;
            for (; pA != null & pB != null; ){
                if (deltaLength > 0) {
                    pB = pB.next;
                    deltaLength--;
                }
                else{
                    if (pA == pB)
                        return pB;
                    pA = pA.next;
                    pB = pB.next;
                }
            }
        }
        return null;
    }

}
