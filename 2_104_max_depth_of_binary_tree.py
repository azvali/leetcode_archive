def maxDepth(self, root: Optional[TreeNode]) -> int:
    
    stack = [[root, 1]]
    res = 0

    while stack:
        node, level = stack.pop()

        if node:
            res = max(res, level)
            stack.append([node.left, level + 1])
            stack.append([node.right, level + 1])

    
    return res
        