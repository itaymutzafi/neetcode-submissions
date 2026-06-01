from collections import deque

class Node:
    def __init__(self, val, minimum):
        self.val = val
        self.minimum = minimum

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = self.stack[-1].minimum if self.stack else val
        node = Node(val, min(curr_min, val))
        self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1].val

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1].minimum
        
        
