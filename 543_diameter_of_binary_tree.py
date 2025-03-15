def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
    self.res = 0

    def dfs(root):

        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)

        self.res = max(self.res, left + right)
        return 1 + max(left, right)

    dfs(root)
    return self.res