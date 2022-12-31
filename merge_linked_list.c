/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    if (list1 == NULL)
        return list2;
    if (list2 == NULL)
        return list1;
    struct ListNode* merged_list = NULL;
    if (list1->val <= list2->val)
    {
        merged_list = list1;
        list1 = list1->next;
    }
    else
    {
        merged_list = list2;
        list2 = list2->next;
    }
    struct ListNode* merged_tail = merged_list;

    while(list1 != NULL && list2 != NULL)
    {
        struct ListNode* temp = NULL;
        if (list1->val <= list2->val)
        {
            temp = list1;
            list1 = list1->next;
        }
        else
        {
            temp = list2;
            list2 = list2->next;
        }
        merged_tail->next = temp;
        merged_tail = temp;
    }
    if (list1 != NULL)
        merged_tail->next = list1;
    else if (list2 != NULL){
        merged_tail->next = list2;
    }
    return merged_list;
}
