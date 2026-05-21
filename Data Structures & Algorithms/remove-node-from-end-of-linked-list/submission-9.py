# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return

        # [1,2,3,4] , 2
        # fast = 1, i =1
        # fast = 2, i = 2
        # fast = 3, i = 3 -> end!
        # but slow is in dummy 
        # until fast is None:
        # slow is 1, slow is 2
        # and then slow is in the right position

        # [1,2], 2
        # fast = dummy, i = 0
        # fast = 1, i = 1
        # fast = 2, i = 2
        # fast = None, i= 3
        # then fast = fast.next => None
        # and slow is not moving, still the dummy
        
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy
        
        i = 0
        while i <= n:
            fast = fast.next
            i +=1
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next # the fast does len(L) - n steps before it reaches none
        return dummy.next

        