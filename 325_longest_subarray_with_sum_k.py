def longest_subarray_sum_k(nums: list[int], k: int) -> int:
    
    prefixsum = {}
    sum = 0
    res = 0
    
    
    for x in range(len(nums)):
        sum += nums[x]
        
        if sum not in prefixsum:
            prefixsum[sum] = x
        
        if sum == k:
            res = max(res, x + 1)
            
        diff = sum - k
        
        if diff in prefixsum:
            res = max(x - prefixsum[diff] , res)


    return res

        
        

    
    
    
    
    
