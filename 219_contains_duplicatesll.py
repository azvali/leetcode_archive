def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    
    
    rangeWindow = set()
    
    for x in range(len(nums)):
        
        if nums[x] in rangeWindow:
           return True
        elif x >= k:
            rangeWindow.remove(nums[x - k - 1])
        
        rangeWindow.add(nums[x])
    
    return False

            
