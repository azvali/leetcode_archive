def findDuplicates(nums: list[int]) -> list[int]:
    
    
    hashmap = {}
    res = []
    
    for x in range(len(nums)):
        hashmap[nums[x]] = hashmap.get(nums[x],0) + 1

    
    for x in hashmap:
        if hashmap[x] == 2:
            res.append(x)
    
    return res