def two_sum(nums: list[int], target: int) -> list[int]:
    
    hashmap = {}

    for x in range(len(nums)):
        
        diff = target - nums[x]
        
        if diff in hashmap:
            return[x,hashmap[diff]]
        
        hashmap[nums[x]] = x
        
    return []
        
        
        
