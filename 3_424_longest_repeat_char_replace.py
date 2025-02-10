def characterReplacement(s: str, k: int) -> int:

    
    hashmap = {}
    l , r = 0 , 0
    res = 0
    
    while r < len(s):
        hashmap[s[r]] = hashmap.get(s[r], 0) + 1
        mostSeen = max(hashmap.values())
        
        while (r - l + 1) - mostSeen > k:
            hashmap[s[l]] -= 1
            l += 1
            
        res = max(res, r - l + 1)
        r += 1
        
    return res
        