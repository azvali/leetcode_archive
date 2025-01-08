def subarraySum(nums: List[int], k: int) -> int:
    
    hashmap = {0 : 1}
    res = 0
    cursum = 0
    
    for x in nums:
        cursum += x
        diff = cursum - k
        
        if diff in hashmap:
            res += hashmap[diff]
            
        hashmap[cursum] = hashmap.get(cursum, 0) + 1
            
            
            
    return res
            
            
            
            
            
