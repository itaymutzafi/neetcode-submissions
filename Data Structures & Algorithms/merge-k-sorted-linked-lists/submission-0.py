# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(node.val, i) for i, node in enumerate(lists)]
        heapq.heapify(h) # heap that is ordered by the vals of the k lists given
        dummy = ListNode()
        tmp = dummy
        
        while h:
            min_i = heapq.heappop(h)[1]
            tmp.next = lists[min_i]
            tmp = tmp.next
            lists[min_i] = lists[min_i].next
            if lists[min_i]:
                heapq.heappush(h, (lists[min_i].val, min_i))
            
            
        return dummy.next
        
        
                
        