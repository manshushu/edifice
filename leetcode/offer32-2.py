import collections
class Solution:
    def levelOrder(self,root:TreeNode) ->list[list[int]]:
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