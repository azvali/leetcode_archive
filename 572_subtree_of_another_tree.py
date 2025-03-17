def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    

    if not root and subRoot or root and not subRoot:
        return False
    
    if not root and not subRoot:
        return True

    if root.val == subRoot.val:

        def checkequal(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root and subRoot or root and not subRoot:
                return False
    
            if root.val != subRoot.val:
                return False
            else:
                return checkequal(root.left, subRoot.left) and checkequal(root.right, subRoot.right)

        if checkequal(root, subRoot) == True:
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    else:
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)