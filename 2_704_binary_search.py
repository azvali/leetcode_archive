def search(nums: list[int], target: int) -> int:
    
    l , r = 0 , len(nums) - 1
    
    
    while l <= r:
        cur = l + (r - l) // 2
        
        if target > nums[cur]:
            l = cur + 1
        elif target < nums[cur]:
            r = cur - 1
        else:
            return cur
            
    return -1