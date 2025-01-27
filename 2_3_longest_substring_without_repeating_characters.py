class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashset = set()
        res = 0
        l,r = 0,0
        
        if len(s) <= 1:
            return len(s)
        
        while r < len(s):
            
            if s[r] not in hashset:
                hashset.add(s[r])
                r += 1
                cur = r - l
                res = max(res, cur)
            else:
                while s[r] in hashset:
                    hashset.remove(s[l])
                    l += 1
                    
        return res
                
