def goodNodes(self, root: TreeNode) -> int:
    
    if not root:
        return None

    self.res = 0

    def dfs(node, maxseen):

        if not node:
            return

        if node.val >= maxseen:
            self.res += 1
        
        
        newmax = max(maxseen, node.val)
        dfs(node.left, newmax)
        dfs(node.right, newmax)

    
    dfs(root, root.val)

    return self.res