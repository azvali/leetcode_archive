def longestSubarray(nums: List[int]) -> int:
    
    
    count0 = 0
    res = 0
    
    l,r = 0 , 0 
    
    while r < len(nums):
        
        if nums[r] == 0:
            count0 += 1
        
        while count0 > 1:
            if nums[l] == 0:
                count0 -= 1
            l += 1
            
        res = max(res, r - l)
        r += 1
        
        
    return res