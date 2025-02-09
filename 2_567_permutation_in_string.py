def checkInclusion(self, s1: str, s2: str) -> bool:
        

    l, r = 0, 0
    hashmap1 = {}
    hashmap2 = {}
        
    for x in range(len(s1)):
        hashmap1[s1[x]] = hashmap1.get(s1[x], 0) + 1

    while r < len(s2):
        if s2[r] not in hashmap1:
            r += 1
            l = r
            hashmap2 = {}
            continue
        else:
            hashmap2[s2[r]] = hashmap2.get(s2[r], 0) + 1

            while hashmap2[s2[r]] > hashmap1[s2[r]]:
                hashmap2[s2[l]] -= 1
                if hashmap2[s2[l]] == 0:
                    del hashmap2[s2[l]]
                l += 1

            if hashmap2 == hashmap1:
                return True

            r += 1

    return False

            

