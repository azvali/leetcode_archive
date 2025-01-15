def subarraySum(nums: list[int], k: int) -> int:

    res = 0
    prefixsum = {0 : 1}
    cur = 0
    
    for x in nums:
        cur += x
        diff = cur - k
        
        if diff in prefixsum:
            res += prefixsum[diff]
        
        prefixsum[cur] = prefixsum.get(cur, 0) + 1
        
    return res