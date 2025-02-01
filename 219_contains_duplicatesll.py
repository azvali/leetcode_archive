def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    
    
    rangeWindow = set()
    
    for x in range(len(nums)):
        
        if nums[x] in rangeWindow:
           return True
       
        rangeWindow.add(nums[x])
       
        if x >= k:
            rangeWindow.remove(nums[x - k - 1])
        
        
    
    return False

            
