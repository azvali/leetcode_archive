def findFirstOccurrence(nums: list[int], target: int) -> int:
    l , r = 0 , len(nums) - 1
    
    
    while l <= r:
        cur = (l + r) // 2
        
        if target > nums[cur]:
            l = cur + 1
        elif target < nums[cur]:
            r = cur - 1
        elif cur > 0 and nums[cur] == nums[cur - 1]:
            r = cur - 1 
        else:
            return cur
    return -1
        
        
        
        
        
        
        
        
        
