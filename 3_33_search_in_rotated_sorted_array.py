def search(self, nums: List[int], target: int) -> int:
    
    def findPivot(nums):
        l , r = 0 , len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
                
        return l
    
    
    l , r = 0 , len(nums) - 1
    piv = findPivot(nums)
    
    if target <= nums[r]:
        l = piv
        r = len(nums) - 1
    else:
        l = 0
        r = piv - 1
        
    while l <= r:
        mid = l + (r - l) // 2
        
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
        
    return -1
        