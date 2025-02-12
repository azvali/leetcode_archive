def totalFruit(fruits: List[int]) -> int:
    
    
    hashmap = {}
    l , r = 0 , 0
    res = 0
    
    while r < len(fruits):
        hashmap[fruits[r]] = hashmap.get(fruits[r], 0) + 1
        
        while len(hashmap) > 2:
            hashmap[fruits[l]] -= 1
            if hashmap[fruits[l]] == 0:
                del hashmap[fruits[l]]
            l += 1
        
        res = max(res, r - l + 1)
        r += 1
        
    return res