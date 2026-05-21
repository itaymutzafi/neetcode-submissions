# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(node.val, id(node), node) for node in lists if node]
        heapq.heapify(h) # heap that is ordered by the vals of the k lists given
        dummy = ListNode()
        tmp = dummy
        
        while h:
            min_node = heapq.heappop(h)[2]
            tmp.next = min_node
            tmp = tmp.next
            next_node = min_node.next
            if next_node:
                heapq.heappush(h, (next_node.val, id(next_node), next_node))
            
        return dummy.next
        
        
                
        