/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode* current = head;
    struct ListNode* temp;

    if (current == NULL){
        return NULL;
    }
    
    while (current->next != NULL)
    {
        if (current->val == current->next->val)
        {
            temp = current->next->next;
            free(current->next);
            current->next = temp;
        }
        else{
            current = current->next;
        }
    }
    return head;
}
