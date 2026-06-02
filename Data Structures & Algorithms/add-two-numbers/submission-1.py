# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = False
        dummy = ListNode() 
        res = dummy 

        while l1 or l2 or extra:
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
            if l2:
                val2 = l2.val

            tmp = val1 + val2 + extra
            if tmp >= 10:
                extra = True
            else:
                extra = False
            res.next = ListNode(tmp % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res = res.next
        
        return dummy.next