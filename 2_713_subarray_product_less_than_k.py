def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    
    
    l,r = 0 , 0 
    res = 0
    cur = 1
    
    while r < len(nums):
        cur *= nums[r]
        
        while cur >= k and l <= r:
            cur /= nums[l]
            l += 1
            
        res += r - l + 1
        
        r += 1