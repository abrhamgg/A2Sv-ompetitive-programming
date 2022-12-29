/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head){
    int n = 0;
    struct ListNode* current = head;
    while (head != NULL)
    {
        n++;
        head = head->next;
    }
    int idx = n /2 + 1;
    int i = 0;
    for (i = 0; i < idx -1; i++) {
        current = current->next;
    }
    return current;
}