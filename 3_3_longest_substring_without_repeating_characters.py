def lengthOfLongestSubstring(self, s: str) -> int:
    
    res = 0
    
    l = 0
    hashmap = {}
    
    for r in range(len(s)):
        hashmap[s[r]] = hashmap.get(s[r], 0) + 1
        
        while hashmap[s[r]] > 1:
            hashmap[s[l]] -= 1
            if hashmap[s[l]] == 0:
                del hashmap[s[l]]
            l += 1
            
        res = max(res, r - l + 1)
        
    return res