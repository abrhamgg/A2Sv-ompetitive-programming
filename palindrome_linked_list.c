/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverse(struct ListNode **head)
{
    struct ListNode* node = *head;
    struct ListNode* next = NULL;
    struct ListNode* prev = NULL;

    while(node)
    {
        next = node->next;
        node->next = prev;
        prev = node;
        node = next;
    }
    *head = prev;
    return *head;

}
bool isPalindrome(struct ListNode* head){
    struct ListNode* temp;
    int size = 0;
    int i;

    if (head == NULL || head->next == NULL)
        return true;
    temp = head;

    while (temp)
    {
        size++;
        temp = temp->next;
    }
    temp = head;
    for (i = 0; i < (size/ 2) - 1; i++)
        temp = temp->next;
    if (size % 2 ==0 && temp->val != temp->next->val)
        return false;
    temp = temp->next->next;
    struct ListNode* rev = reverse(&temp);
    struct ListNode* mid = rev;

    temp = head;
    while(rev) {
        if (temp->val != rev->val)
            return false;
        temp = temp->next;
        rev = rev->next;
    }
    reverse(&mid);
    return true;
}
