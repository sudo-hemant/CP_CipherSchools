


class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    

    def push(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    
    def pop(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            popped = self.head
            self.head = self.tail = None
        else:
            popped = self.head
            self.head = self.head.next

        return popped.value
            

    def is_empty(self):
        return self.head == None


    def top(self):
        if not self.head:
            return None
        return self.head.value


    def reverse(self):
        prev, curr = None, self.head

        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next

        self.head, self.tail = prev, self.head


    def print_queue(self):
        iterater = self.head

        while iterater:
            print(iterater.value)
            iterater = iterater.next


queue = Queue()

queue.push(10)
queue.push(20)
queue.push(30)
queue.push(40)

queue.pop()
print(queue.is_empty())
print(queue.top())

print()

queue.print_queue()

queue.reverse()
print()

queue.print_queue()
