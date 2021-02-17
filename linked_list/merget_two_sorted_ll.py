
# https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1/?track=DSASP-LinkedList&batchId=154

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


def sortedMerge(head_A, head_B):
    if not head_A and not head_B:
        return
    elif not head_A:
        return head_B
    elif not head_B:
        return head_A
    else:
        if head_A.data <= head_B.data:
            head = head_A
            tail = head_A
            a = head_A.next
            b = head_B
        else:
            head = head_B
            tail = head_B
            a = head_B.next
            b = head_A
            
        while a and b:
            if a.data <= b.data:
                tail.next = a
                tail = tail.next
                a = a.next
            else:
                tail.next = b
                tail = tail.next
                b = b.next
        if a is not None:
            tail.next = a
        else:
            tail.next = b
    return head
            
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3
# Node Class
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
        
# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, input().strip().split())
        
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        
        for x in nodes_a:
            a.append(x)
        
        for x in nodes_b:
            b.append(x)
        
        printList(sortedMerge(a.head,b.head))

# } Driver Code Ends