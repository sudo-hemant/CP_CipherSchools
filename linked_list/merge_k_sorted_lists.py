
# https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1/?track=DSASP-LinkedList&batchId=154



def mergeKLists(arr,N):
    # if len(arr) == 1:
    #     return arr[0]
        
    # head_returned = merge(arr[0], arr[1])

    # for i in range(2, len(arr)):
    #     head_returned = merge(arr[i], head_returned)
        
    # return head_returned
    
    last = N - 1
    while last != 0:
        i, j = 0, last
        
        while i < j:
            arr[i] = merge(arr[i], arr[j])
            i, j = i + 1, j - 1
            
            if i >= j:
                last = j
                
    return arr[0]
    
    
def merge(first, second):
    dummy = Node(0)
    curr = dummy
    
    while first and second:
        if first.data <= second.data:
            curr.next = first
            first = first.next
        else:
            curr.next = second
            second = second.next
        curr = curr.next
        
    if not first:
        curr.next = second
    else:
        curr.next = first
    
    return dummy.next
        





#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = mergeKLists(heads,n)
        printList(merged_list)
