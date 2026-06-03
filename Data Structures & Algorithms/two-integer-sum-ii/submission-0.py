class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,2,3,4], 3
        # 1 -> need to find 2.
        # 2 -> need to find 1, so this is not possible.
        # 3 -> need to find 0, so this is not possible
        # if target - numbers[i] < numbers[i] so this I have already seen this number
        # O(nlogn)
        
        def binary_search(start, target):
            l, r = start, len(numbers) - 1
            
            while l <= r:
                mid = (r + l) // 2
                if numbers[mid] == target:
                    return mid
                if numbers[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1        
            return -1

        for i in range(len(numbers)):
            if (target - numbers[i]) > numbers[i]:
                j = binary_search(i + 1, target - numbers[i])
                if j != -1:
                    return [i+1, j+1]
        