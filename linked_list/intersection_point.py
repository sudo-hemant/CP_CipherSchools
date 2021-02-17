
# https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1/?track=DSASP-LinkedList&batchId=154



def intersetPoint(head_a,head_b):
    
    if head_a is None or head_b is None:
        return -1
    
    count_a = count_b = 0
    curr_a, curr_b = head_a, head_b
    difference_size = 0
    
    count_a = count(head_a)
    count_b = count(head_b)

    if count_a >= count_b:
        small, large = head_b, head_a
        difference_size = count_a - count_b
    else:
        small, large = head_a, head_b
        difference_size = count_b - count_a
        
    advance_large = large
    while difference_size:
        advance_large = advance_large.next
        difference_size -= 1
        
    curr_small, curr_large = small, advance_large
    while curr_small != curr_large:
        curr_small, curr_large = curr_small.next, curr_large.next
        
    if curr_small is None:
        return -1
        
    return curr_small.data
    
    

def count(head):
    curr = head
    count = 0
    
    while curr:
        count += 1
        curr = curr.next
    
    return count


import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        temp=None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        x,y,z = map(int,input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node=Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node=Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node=Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i== 0:
                b.append(node)  # add to the end of the list b, only the intersection
        
        print(intersetPoint(a.head,b.head))

