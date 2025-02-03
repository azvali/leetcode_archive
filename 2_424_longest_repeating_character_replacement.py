def characterReplacement(self, s: str, k: int) -> int:
    
    
    l , r = 0 , 0
    hashmap = {}
    res = 0
    mostfreq = 0
    
    while r < len(s):
        
        hashmap[s[r]] = hashmap.get(s[r] , 0) + 1
        mostfreq = max(mostfreq, hashmap[s[r]])
        
        
        while (r - l + 1) - mostfreq > k:
            hashmap[s[l]] -= 1
            if hashmap[s[l]] == 0:
                del hashmap[s[l]]
            l += 1

        res = max(res, r - l + 1)
        r += 1

    return res
    