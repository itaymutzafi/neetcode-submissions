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
        # first step - create the clone
        tmp = head
        while tmp:
            clone = Node(tmp.val)
            tmp_next = tmp.next
            tmp.next = clone
            clone.next = tmp_next
            tmp = tmp_next

        tmp = head
        new_head = head.next

        while tmp and tmp.next:
            tmp.next.random = tmp.random.next if tmp.random else None
            tmp = tmp.next.next
        
        tmp = head

        while tmp:
            copy = tmp.next
            tmp.next = tmp.next.next
            if copy.next:
                copy.next = copy.next.next
            tmp = tmp.next

        return new_head
        
            