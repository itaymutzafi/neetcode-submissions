# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            tmp_next = head.next
            head.next = prev
            prev = head
            head = tmp_next
        return prev
    
    def mergeLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        res = head1

        # [1,2,3] , [4,5,6]
        # [1,4,2] , head1 = 1, head2 = 4 -> head1 = 2, head2 = 5
        # [1,4,2,5,3], head1 = 2, head2 = 5 -> head1 = 3, head2 = 6
        # [1,4,2,5,3,6], head1 = 3, head2 = 6, head1 = None, head2 = None

        # [1,2,3], [4,5,6,7] -> what happened?
        # [1,4,2] , head1 = 1, head2 = 4 -> head1 = 2, head2 = 5
        # [1,4,2,5,3], head1 = 2, head2 = 5 -> head1 = 3, head2 = 6
        # [1,4,2,5,3,6], head1 = 3, head2 = 6, head1 = None, head2 = 7
        # [1,4,2,5,3,6,None]
        
        while head1 and head2:
            tmp_1 = head1.next
            tmp_2 = head2.next
            head1.next = head2
            if tmp_1:
                head2.next = tmp_1
            head1 = tmp_1
            head2 = tmp_2
        
        return res.next
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        slow = fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
          
        # slow is the middle, prev is the last before the middle
        
        mid = self.reverseList(slow)
        if prev:
            prev.next = None # disconnect the middle and the original list
        self.mergeLists(head, mid)

        
            