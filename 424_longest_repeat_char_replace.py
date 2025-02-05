def characterReplacement(s: str, k: int) -> int:

    
    hashmap = {}
    l = 0
    res = 0
    
    for r in range(len(s)):
        
        hashmap[s[r]] = hashmap.get(s[r], 0) + 1
        mostseen = max(hashmap.values())
        
        if (r - l + 1) - mostseen > k:
            hashmap[s[l]] -= 1
            if hashmap[s[l]] == 0:
                del hashmap[s[l]]
            l += 1
            
        res = max(res, (r - l + 1))

    return res