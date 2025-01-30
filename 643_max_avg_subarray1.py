def findMaxAverage(nums: List[int], k: int) -> float:


    l,r  = 0, 0
    res = float('-inf')
    cur = 0
    
    while r < k:
        cur += nums[r]
        r += 1
    
    res = max(res, cur / k)
        
        
    while r < len(nums):
        cur += nums[r]
        cur -= nums[l] 
        res = max(res, cur / k )
        r += 1
        l += 1
        
    return res