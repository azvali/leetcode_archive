def top_k_frequent(nums: list[int], k: int) -> list[int]:
    
    hashmap = {}
    
    for x in nums:
        
        hashmap[x] = hashmap.get(x, 0) + 1

    res = []
    
    while k > 0:
        curmax = max(hashmap, key=hashmap.get)
        res.append(curmax)
        del hashmap[curmax]
        k -= 1
    
    return res
    
    
