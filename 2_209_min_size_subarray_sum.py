def minSubArrayLen(target: int, nums: List[int]) -> int:
    
    
    res = float('inf')
    l = 0
    cur = 0
    
    for r in range(len(nums)):
        
        cur += nums[r]
        
        while cur >= target:
            arrlen = (r - l) + 1
            res = min(res, arrlen)
            cur -= nums[l]
            l += 1
    
    return res if res != float('inf') else 0
        
        