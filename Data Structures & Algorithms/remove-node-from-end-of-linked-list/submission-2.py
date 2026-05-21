# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            tmp_next = head.next
            head.next = prev
            prev = head
            head = tmp_next
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: # case of len(L) == 1
            return

        rev_head = self.reverseList(head)
        node = rev_head
        i = 1
        prev = None

        while i < n:
            prev = node
            node = node.next
            i +=1
        
        if prev:
            prev.next = node.next
        else:
            rev_head = node.next
        
        return self.reverseList(rev_head)

        