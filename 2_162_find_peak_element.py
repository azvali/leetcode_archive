def findPeakElement(nums):
    
    l , r = 0 , len(nums) - 1
    
    while l < r:
        cur = l + (r - l) // 2
        
        if nums[cur] > nums[cur + 1]:
            r = cur
        else:
            l = cur + 1
            
    return l