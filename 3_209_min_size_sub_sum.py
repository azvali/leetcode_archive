def minSubArrayLen(target: int, nums: List[int]) -> int:

    l , r = 0 , 0
    cur = 0
    res = float('inf')
    
    while r < len(nums):
        cur += nums[r]
        
        while cur >= target:
            res = min(res, r - l + 1)
            cur -= nums[l]
            l += 1
            
        r += 1
        
    return res if res != float("inf") else 0