
class Node:
    def __init__(self, value = None, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def push_front(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def push_back(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def pop_front(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            popped = self.head
            self.head = self.tail = None
        else:
            popped = self.head
            self.head.next.prev = None
            self.head = self.head.next
        
        return popped.value


    def pop_back(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            popped = self.head
            self.head = self.tail = None
        else:
            popped = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev

        return popped.value


    def is_empty(self):
        return self.head == None


    def top(self):
        if not self.head:
            return None
        return self.head.value


    def reverse(self):
        pass


    def print_deque(self):
        iterater = self.head

        while iterater:
            print(iterater.value)
            iterater = iterater.next




deque = Deque()

deque.push_front(10)
deque.push_front(5)
deque.push_front(0)

deque.print_deque()        

deque.push_back(20)
deque.push_back(30)
deque.push_back(40)

print()
deque.print_deque()        
print()

print(deque.pop_back())
print(deque.pop_front())

print()
deque.print_deque()        
print()


print(deque.top())
print(deque.is_empty())