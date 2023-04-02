class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self,root:TreeNode)-> int:
        if not root: return 0
        queue,res=[root],0
        while queue:
            tmp=[]
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue=tmp
            res+=1
        return res