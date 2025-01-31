def characterReplacement(s: str, k: int) -> int:

    hashmap = {}
    l, r = 0, 0
    res = 0
    maxfreq = 0
    
    while r < len(s):
        hashmap[s[r]] = hashmap.get(s[r],0) + 1
        maxfreq = max(maxfreq, hashmap[s[r]])
        
        while (r - l + 1) - maxfreq > k:
            hashmap[s[l]] = hashmap.get(s[l], 0) - 1
            if hashmap[s[l]] == 0:
                del hashmap[s[l]]
            l += 1
        
        res = max(res , r - l + 1)
        r += 1
        
        
    return res