class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(L, tmp):
            if len(L) == len(nums):
                res.append(L.copy())
                return
            for i in range(len(tmp)):
                L.append(tmp[i])
                curr = tmp.pop(i)
                helper(L, tmp)
                L.pop()
                tmp.insert(i, curr)
        
        helper([], nums.copy())
        return res

                # [1] -> [1,2]
                # [1,2] -> [1,2,3]
                # [1,2] -> end
                # [1] -> [1,3]
                # [1,3] -> [1,3,2]
                # [1,3] -> end
                # [1] -> end
                # [2] -> [2,1]
                
                