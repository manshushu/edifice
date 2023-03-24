import collections
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self,root:TreeNode)->List[List[int]]:
        if not root: return []
        res,deque=[], collections.deque([root])
        while deque:
            tmp= collections.deque()
            for _ in range(len(deque)):
                node=deque.popleft()
                if len(res) % 2 ==0: tmp.append(node.val)
                else:tmp.appendleft(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp))
        return res