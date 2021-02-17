
# https://leetcode.com/problems/reorder-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def reorderList(self, head: ListNode) -> None:
        
        if not head or not head.next or not head.next.next:
            return
        
        end_first_half = self.partition_list(head)
        
        temp = end_first_half.next
        end_first_half.next = None
        
        second_head = self.reverse_second_half(temp)
        
        self.reorder_list_util(head, second_head)
    
    
    def partition_list(self, head):
        
        slow, fast = head, head.next
        
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        
        if fast.next:
            slow = slow.next
        
        return slow
        
    def reverse_second_half(self, head):
        prev, curr = None, head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev
    

    def reorder_list_util(self, head_1, head_2):
        
        dummy_head = ListNode()
        current = dummy_head

        while head_1 or head_2:
            if head_1:
                current.next = head_1
                head_1 = head_1.next
                current = current.next
            if head_2:
                current.next = head_2
                head_2 = head_2.next
                current = current.next
                
        
        
        