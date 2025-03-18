def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
                
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        lenq = len(q)
        rightSide = None

        for i in range(lenq):
            n = q.popleft()
            if n:
                rightSide = n
                q.append(n.left)
                q.append(n.right)
        
        if rightSide:
            res.append(rightSide.val)

    return res