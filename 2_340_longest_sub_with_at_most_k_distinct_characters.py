def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    
    
    freq = {}
    res = 0
    l = 0
    
    for r in range(len(s)):
        freq[s[r]] = freq.get(s[r], 0) + 1
        
        if len(freq) > k:
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l += 1
            
        res = max(res, r - l + 1)

    return res