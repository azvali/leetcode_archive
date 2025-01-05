class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(nums):
            l, r = 0, len(nums) - 1
            while l < r:
                cur = (l + r) // 2

                if nums[cur] > nums[r]:
                    l = cur + 1
                else:
                    r = cur
            return l
                    
        
        l, r = 0, len(nums) - 1
        pivot = findPivot(nums)

        if nums[pivot] <= target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            cur = (l + r) // 2

            if nums[cur] > target:
                r = cur - 1
            elif nums[cur] < target:
                l = cur + 1
            elif nums[cur] == target:
                return cur
            
        return -1

        
        
        
        
        
        
        
        
        
        
