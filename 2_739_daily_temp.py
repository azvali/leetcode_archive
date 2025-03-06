def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
    stack = [] # store in [temp, index] format
    res = [0] * len(temperatures)

    for i , temp in enumerate(temperatures):
        while stack and stack[-1][0] < temp:
            stemp , sind = stack.pop()
            res[sind] = (i - sind)
        stack.append([temp, i])
    
    return res
            