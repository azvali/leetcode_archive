def checkInclusion(self, s1: str, s2: str) -> bool:
        
    s1freq = {}
    hashmap = {}
    l,r  = 0, 0

    for x in range(len(s1)):
        s1freq[s1[x]] = s1freq.get(s1[x], 0) + 1

    while r < len(s2):
        hashmap[s2[r]] = hashmap.get(s2[r], 0) + 1

        if hashmap == s1freq:
            return True
       
        if r - l + 1 >= len(s1):
            hashmap[s2[l]] -= 1
            if hashmap[s2[l]] == 0:
                del hashmap[s2[l]]
            l += 1

        r += 1

    return False
        