def search(nums, target):
    
    
    def findPivot(nums):
        l , r = 0 , len(nums) - 1
        
        
        while l < r:
            
            cur = l + (r - l) // 2
            
            if nums[cur] > nums[r]:
                l = cur + 1
            else:
                r = cur
                
        return l
        
        
    l , r = 0 , len(nums) - 1
    pivot = findPivot(nums)
    
    if target < nums[r]:
        l = pivot
        r = len(nums) - 1
    else:
        l = 0
        r = pivot - 1
        
    while l <= r:
        mid = l + (r - l) // 2
        
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    
    return -1