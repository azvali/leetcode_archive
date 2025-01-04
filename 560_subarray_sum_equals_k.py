def subarraySum(nums, k):

    hashmap = {0 : 1}
    sum = 0
    res = 0
    
    for x in nums:
        
        sum += x
        
        diff = sum - k
        
        if diff in hashmap:
            res += hashmap[diff]
        
        hashmap[sum] = hashmap.get(sum, 0) + 1
        
    return res
            
        
        
