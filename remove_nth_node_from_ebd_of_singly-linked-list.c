/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    int len = 0;
    struct ListNode* current = head;
    struct ListNode* temp = head;
    while (current != NULL)
    {
        len++;
        current = current->next;
    }
    current = head;
    //printf("%i\n", len);
    int idx = len - n;
    if (len == n)
    {
        head = head->next;
        free(current);
        return (head);
    }
    if (n == 1)
    {
        while (current->next->next != NULL)
        {
            current = current->next;
        }
        current->next = NULL;
        return head;
    }
    for (int i = 0; i < (len - n - 1); i++)
        current = current->next;

    temp = current->next;
    current->next = temp->next;
    free(temp);
    return head;

}