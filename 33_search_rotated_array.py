def search(self, nums: List[int], target: int) -> int:


    def findpivot(nums):
        l , r = 0 , len(nums) - 1
        mid = 0
        while l < r:
            mid = l + (r-l) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return l
    
    
    pivot = findpivot(nums)
    l , r = 0 , len(nums) - 1
    
    if target <= nums[r]:
        l , r = pivot, len(nums) - 1
    else:
        l , r = 0 , pivot - 1
        
    while l <= r:
        mid = l + (r - l) // 2
        
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
        
    return -1
        
        