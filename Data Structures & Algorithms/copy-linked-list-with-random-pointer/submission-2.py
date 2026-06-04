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
        d = {None: None}
       
        tmp = head
        while tmp:
            if tmp not in d:
                d[tmp] = Node(tmp.val)                
            if tmp.next not in d:
                d[tmp.next] = Node(tmp.next.val)
            if tmp.random not in d:
                d[tmp.random] = Node(tmp.random.val)
            
            d[tmp].next = d[tmp.next]
            d[tmp].random = d[tmp.random]
            
            tmp = tmp.next
        
        return d[head]
        
        
            