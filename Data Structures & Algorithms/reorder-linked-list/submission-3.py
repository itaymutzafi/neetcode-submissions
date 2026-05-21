# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = head
        stack = []
        while node:
            stack.append(node)
            node = node.next
        if len(stack) == 1:
            return
        
        odd = len(stack) % 2 != 0
        i = 0 
        j = len(stack) - 1

        while i < j:
            tmp_next = head.next
            head.next = stack.pop()
            head = head.next
            head.next = tmp_next
            head = head.next
            i +=1
            j -=1
        
        if odd and stack:
            head.next = stack.pop()
            head = head.next
        
        head.next = None       
            