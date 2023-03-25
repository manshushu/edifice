import collections
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self,root:'TreeNode',sum:'int')->List[List[int]]:
        res,path=[],[]
        def recur(root,tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar ==0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left,tar)
            recur(root.right,tar)
            path.pop()
        recur(root,sum)
        return res