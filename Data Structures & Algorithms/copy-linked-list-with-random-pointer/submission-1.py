"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        d = {}

        tmp = head
        while tmp:
            new = Node(tmp.val)
            d[tmp] = new
            tmp = tmp.next
        
        tmp = head
        while tmp:
            d[tmp].next = d[tmp.next] if tmp.next else None
            d[tmp].random = d[tmp.random] if tmp.random else None
            tmp = tmp.next
        
        return d[head]
        
        
            