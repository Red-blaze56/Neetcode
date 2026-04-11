/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head == nullptr || head->next == nullptr)
            return true;
            
        ListNode* fast=head;
        ListNode* slow=head;

        while(fast && fast->next){
            fast=fast->next->next;
            slow=slow->next;
        }
        ListNode* head2 = reverseLinkedList(slow);
        ListNode* head2_start=head2;
        bool ans = checkPalindrome(head,head2);
        reverseLinkedList(head2_start);
        return ans;
    }

    ListNode* reverseLinkedList(ListNode* head){
        ListNode* curr = head;
        ListNode* prev = nullptr;
        while(curr){
            ListNode* NextNode = curr->next;
            curr->next=prev;
            prev=curr;
            curr=NextNode;
        }
        return prev;
    }
    
    bool checkPalindrome(ListNode* head1, ListNode* head2){
        while(head1 && head2){
            if(head1->val!=head2->val){return false;}
            else{head1=head1->next;head2=head2->next;}
        }
        return true;
    }

};