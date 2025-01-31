def maxVowels(s: str, k: int) -> int:

    res = 0
    cur = 0
    l, r = 0, 0
    vowels = {"a","e","i","o","u"}
    while r < k:
        if s[r] in vowels:
            cur += 1
        r += 1
        
    res = max(res, cur)
    
    while r < len(s):
        if s[r] in vowels:
            cur += 1
        if s[l] in vowels:
            cur -= 1
        res = max(res, cur)
        l += 1
        r += 1
    
    return res
    


        
    