def totalFruit(fruits: List[int]) -> int:

    
    res = 0
    l = 0
    hashmap = {}
    
    for r in range(len(fruits)):
        
        hashmap[fruits[r]] = hashmap.get(fruits[r], 0) + 1
        
        while len(hashmap) > 2:
            hashmap[fruits[l]] -= 1
            if hashmap[fruits[l]] == 0:
                del hashmap[fruits[l]]
            l += 1
            
        res = max(res, r - l + 1)
        
    return res