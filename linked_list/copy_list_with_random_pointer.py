
# https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return None
        
        mapping = {}
        
        self.create_nodes(head, mapping)
        self.clone_pointers(head, mapping)
        
        return self.remove_cloned(head)
        
    
    def remove_cloned(self, head):

        dummy_head = Node(0)
        current = head
        dummy_current = dummy_head
        
        while current:
            dummy_current.next = current.next
            current.next = current.next.next
            current = current.next
            dummy_current = dummy_current.next
            
        return dummy_head.next
        
    
    def create_nodes(self, head, mapping):
        
        current = head
        
        while current:
        
            new_node = Node(current.val, current.next)
            current.next = new_node
            mapping[current] = new_node
            current = current.next.next
            
    
    def clone_pointers(self, head, mapping):
        
        current = head
        
        while current:
            
            if current.random == None:
                current.next.random = None
            else:
                mapping[current].random = mapping[current.random]
    
            current = current.next.next