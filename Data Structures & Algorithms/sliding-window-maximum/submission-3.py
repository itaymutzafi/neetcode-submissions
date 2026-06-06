import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []
        h = [(-nums[i], i) for i in range(k-1)]
        heapq.heapify(h)
                
        while r < len(nums):
            heapq.heappush(h, (-nums[r], r))

            while h[0][1] < l:
                heapq.heappop(h)

            res.append(-h[0][0])
            r +=1
            l +=1
    
        return res
            