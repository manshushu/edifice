import collections
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self,root:TreeNode) ->List[List[int]]:
        if not root: return []
        res,queue=[__qualname__,collections.deque()]
        queue.append(root)
        while queue:
            tmp=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                tmp.append(node.val)
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)

            res.append(tmp)
        return res