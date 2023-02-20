class Stack:
    def __init__(self):
        self.q = []
        self.min_vals = []
        
    def push(self, item):
        size = len(self.q)
        self.q.append(item)
        
        if size == 0 or item <= self.min_vals[-1]:
            self.min_vals.append(item)
            
        for i in range(size):
            self.q.append(self.q.pop(0))
            
    def pop(self):
        if self.is_empty():
            return None
        if self.q[0] == self.min_vals[-1]:
            self.min_vals.pop()
        
        return self.q.pop(0)
    
    def top(self):
        if self.is_empty():
            return None
        return self.q[0]
    
    def minimum(self):
        if self.is_empty():
            return None
        return self.min_vals[-1]
    
    def is_empty(self):
        return len(self.q) == 0

stack = Stack()

print("push")
print("Pop")
print("top")
print("Minimum")
print("Quit")

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
    elif operation == "top":
        if stack.is_empty():
            print("Stack is empty")
        else:
            print("Top value:", stack.top())
    elif operation == "minimum":
        if stack.is_empty():
            print("Stack is empty")
        else:
            print("Minimum value:", stack.minimum())
    elif operation == "quit":
        break
