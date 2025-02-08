def numSubarraysWithSum(nums: List[int], goal: int) -> int:

    cur = 0
    res = 0
    l , r = 0 , 0
    prefixsum = {0 : 1}
    
    while r < len(nums):
        
        cur += nums[r]
        diff = cur - goal
        
        if diff in prefixsum:
            res += prefixsum[diff]
            
            
        prefixsum[cur] = prefixsum.get(cur, 0) + 1
        r += 1
        
    return res