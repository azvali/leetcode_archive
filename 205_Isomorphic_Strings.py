def isIsomorphic(s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        
        for charS, charT in zip(s, t):
            if charS not in hashmap1:
                hashmap1[charS] = charT
            else:
                if hashmap1[charS] != charT:
                    return False
                
            if charT not in hashmap2:
                hashmap2[charT] = charS
            else:
                if hashmap2[charT] != charS:
                    return False
                
        return True
    

