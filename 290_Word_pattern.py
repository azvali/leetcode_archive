def wordPattern(pattern: str, s: str) -> bool:
    
    words = s.split()
        
    if len(pattern) != len(words):  
        return False
        
    hashmap_p_to_w = {}
    hashmap_w_to_p = {}
        
    for p, w in zip(pattern, words):
        if p in hashmap_p_to_w and hashmap_p_to_w[p] != w:
            return False
        if w in hashmap_w_to_p and hashmap_w_to_p[w] != p:
            return False
            
        hashmap_p_to_w[p] = w
        hashmap_w_to_p[w] = p  
        
    return True
    
    
            
            
            
        
            
           
