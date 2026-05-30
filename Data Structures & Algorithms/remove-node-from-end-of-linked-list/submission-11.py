# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 0

        while node:
            length +=1
            node = node.next
                
        i = 0
        new_head = ListNode(0, head)
        prev = new_head
        node = head

        while i < length - n:
            prev = node
            node = node.next
            i +=1
        
        
        prev.next = node.next

        return new_head.next