def findFirstOccurrence(nums: list[int], target: int) -> int:
    l , r = 0 , len(nums) - 1
    first = -1
    
    
    while l <= r:
        cur = (l + r) // 2
        
        if target > nums[cur]:
            l = cur + 1
        elif target < nums[cur]:
            r = cur - 1
        else:
            first = cur
            r = cur - 1
            
    return first
        
        
        
        
        
        
        
        
        
