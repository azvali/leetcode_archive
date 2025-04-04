def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    if not root:
        return None

    def helper(node):

        if not node:
            return None

        node.left , node.right = node.right , node.left

        helper(node.left)
        helper(node.right)
    
    helper(root)

    return root