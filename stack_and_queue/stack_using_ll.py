


class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.head = None


    def push(self, value):
        self.head = Node(value, self.head)


    def pop(self):
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

        self.head = prev


    def print_stack(self):
        iterater = self.head
        
        while iterater:
            print(iterater.value)
            iterater = iterater.next
            


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
# stack.pop()

print(stack.top())
print(stack.is_empty())

stack.print_stack()

stack.reverse()

stack.print_stack()

        
