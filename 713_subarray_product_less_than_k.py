def numSubarrayProductLessThanK(nums, k):
    
    
    
    l = 0
    cur = 1
    res = 0
    
    
    for r in range(len(nums)):
        
        cur *= nums[r]
        
        while cur >= k and l <= r:
            cur /= nums[l]
            l += 1
            
        res += (r - l + 1)
        
    return res
        
   