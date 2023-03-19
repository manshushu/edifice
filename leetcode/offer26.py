class Solution:
    def isSubDtructure(self, A: 'TreeNode', B: 'TreeNode') -> bool:
        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubDtructure(A.left, B) or self.isSubDtructure(A.right, B))
