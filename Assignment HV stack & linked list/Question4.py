class Stack:
    def __init__(self):
        self.q = []
    
    def push(self, item):
        size = len(self.q)
        self.q.append(item)
        for i in range(size):
            self.q.append(self.q.pop(0))
    
    def pop(self):
        if self.is_empty():
            return None
        return self.q.pop(0)
    
    def top(self):
        if self.is_empty():
            return None
        return self.q[0]
    
    def is_empty(self):
        return len(self.q) == 0

stack = Stack()

print("Push an element onto the stack:")
print("Pop the top element from the stack:")
print("Quit the program:")

while True:
    do = input("What would you like to do? ").split()
    operation = do[0].strip().lower()
    if operation == "push":
        stack.push(int(do[1]))
    elif operation == "pop":
        if stack.is_empty():
            print("Stack is empty")
        else:
            print("Popped value:", stack.pop())
    elif operation == "quit":
        break
