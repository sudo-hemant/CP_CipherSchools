

# https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1/?track=DSASP-LinkedList&batchId=154


def isPalindrome(head):
    
    slow, fast = head, head.next
    count = 1
    
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        count += 1
        
    prev, curr = slow, slow.next
    prev.next = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    start, end = head, prev
    while start :
        if start.data != end.data:
            return False
        start, end = start.next, end.next
        
    return True
    

import atexit
import io
import sys

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if isPalindrome(a.head):
            print(1)
        else:
            print(0)
