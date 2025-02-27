def isValid(self, s: str) -> bool:
    stack = []
    hashmap = {']' : '[', '}' : '{' , ')' : '('}

    for x in range(len(s)):

        if s[x] in hashmap:
            if not stack:
                return False
            
            if stack[-1] != hashmap[s[x]]:
                return False

            stack.pop()
            
        else:
            stack.append(s[x])

    return True if len(stack) == 0 else False