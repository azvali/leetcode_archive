def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []

    for x in range(len(asteroids)):
        if asteroids[x] > 0:
            stack.append(asteroids[x])
        else:
            while stack and stack[-1] > 0 and abs(asteroids[x]) > stack[-1]:
                stack.pop()
            if stack and stack[-1] == abs(asteroids[x]):
                stack.pop()
                continue
            if stack and stack[-1] > abs(asteroids[x]):
                continue
            
            stack.append(asteroids[x])
    return stack