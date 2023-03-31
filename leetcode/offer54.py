def dfs(root):
    if not root: return
    dfs(root.left)
    print(root.val)
    dfs(root.right)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargest(self,root:TreeNode,k:'int')-> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k ==0: return
            self.k -=1
            if self.k ==0:self.res=root.val
            dfs(root.left)
        self.k=k
        dfs(root)
        return self.res