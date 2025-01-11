class Codec:
    
    
    
    def encode(self, strs: List[str]) -> str:
        
        encoded_parts = []
        
        for x in strs:
           
           encoded_parts.append(str(len(x)) + "#" + x)
           
        return "".join(encoded_parts)
           
            
            
                
            

    def decode(self, s: str) -> List[str]:
        
        res = []
        x = 0
       
        while x < len(s):
            
            numholder = ""
            
            while s[x] != "#":
                numholder += s[x]
                x += 1
            
            num = int(numholder)
            x += 1
            
            stringholder = s[x : x + num]
            
            res.append(stringholder)
            x += num

        return res        
        
            
            
            
            
            
            
            
            
            
