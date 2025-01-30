def minSubArrayLen(target: int, nums: List[int]) -> int:

    
    l = 0
    res = float('inf')
    cur = 0
    
    for r in range(len(nums)):
        cur += nums[r]
        

        while cur >= target:
            res = min(res, r - l + 1)
            cur -= nums[l]
            l += 1

                
    return res if res != float('inf') else 0
        
        