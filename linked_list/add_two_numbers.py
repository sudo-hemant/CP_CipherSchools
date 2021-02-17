
# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        root = curr = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            curr_val = carry
            
            if l1:
                curr_val += l1.val
                l1 = l1.next
            if l2:
                curr_val += l2.val
                l2 = l2.next
                
            carry = curr_val // 10
            val = curr_val % 10
            curr.next = ListNode(val)
            curr = curr.next
            
        return root.next
                