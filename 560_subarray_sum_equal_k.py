def subarraySum(nums: List[int], k: int) -> int:


    l , r = 0 , 0 
    res = 0
    cur = 0
    prefixsum = {0:1}
    
    while r < len(nums):
        cur += nums[r]
        diff = cur - k
        
        if diff in prefixsum:
            res += prefixsum[diff]
            
        prefixsum[cur] = prefixsum.get(cur, 0) + 1
        r += 1
        
        
    return res
        