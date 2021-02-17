
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return head
        
        dummy = current = ListNode()
        current.next = head
        
        while current.next:
            returned_value = self.reverse(current.next, k)
            
            if not returned_value:
                break
                
            current.next = returned_value
            temp = 0
            while temp < k:
                current = current.next
                temp += 1
                  
        return dummy.next
            
        
    def reverse(self, current, k):
        temp = [] * (k + 1)
        size = 0
        
        while current and size < k:
            temp.append(current)
            current = current.next
            size += 1    
            
        temp.append(current)
            
        if size != k:
            return False
        
        for i in reversed(range(1, len(temp) - 1)):
            temp[i].next = temp[i-1]
        
        temp[0].next = temp[-1]
            
        return temp[-2]
    
    
        