class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *p = l1; 
        ListNode *q = l2;
        ListNode *result = (ListNode*)malloc(sizeof(ListNode) + 1);
        ListNode *s = result;
        
        int shiftValue = 0;
        
        while (true){
            //两个均不为null
            if (p != NULL && q != NULL){
                ListNode *t = (ListNode*)malloc(sizeof(ListNode) + 1);//temporate node
                t->val = (shiftValue + p->val + q->val) % 10;
                shiftValue = (shiftValue + p->val + q->val) / 10;
                s->next = t;
                s = s->next;
                p = p->next;
                q = q->next;
            }
            //p为null而另一个不为null
            else if (p == NULL && q != NULL){
                ListNode *t = (ListNode*)malloc(sizeof(ListNode) + 1);
                t->val = (shiftValue + q->val) % 10;
                shiftValue = (shiftValue + q->val) / 10;
                s ->next = t;
                s = s->next;
                q = q->next;
            }
            else if (p != NULL && q == NULL){
                ListNode *t = (ListNode*)malloc(sizeof(ListNode) + 1);
                t->val = (shiftValue + p->val) % 10;
                shiftValue = (shiftValue + p->val) / 10;
                s ->next = t;
                s = s->next;
                p = p->next;
            }
            else {
                if (shiftValue > 0){
                    ListNode *t = (ListNode*)malloc(sizeof(ListNode) + 1);
                    t -> val = shiftValue; 
                    t -> next = NULL;
                    shiftValue = 0;
                    s -> next = t;
                }
                else{
                    s->next = NULL;
                }
                break;
            }   
        }
        //最后别忘了要 result = result->next一下。
        return result -> next;
    }
};