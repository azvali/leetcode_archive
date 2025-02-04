def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:


    hashmap = {}
    l , r = 0 , 0
    res = 0
    
    
    while r < len(s):
        hashmap[s[r]] = hashmap.get(s[r], 0) + 1
        
        while len(hashmap) > k:
            hashmap[s[l]] -= 1
            if hashmap[s[l]] == 0:
                del hashmap[s[l]]
            l += 1
        
        
        r += 1    
        res = max(res, r - l)
    
    return res