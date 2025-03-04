class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
                
        stack = []
        
        for x in tokens:
            if x in {"+" , "-" , "/" , "*"}:
                a = stack.pop()
                b = stack.pop()
                
                if x == "+":
                    res = a + b
                elif x == "-":
                    res = b - a
                elif x == "*":
                    res = a * b
                elif x == "/":
                    res = int(b / a)
                    
                stack.append(res)
            else:
                stack.append(int(x))
        
        return stack[0]