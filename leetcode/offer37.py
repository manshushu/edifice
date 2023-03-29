import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(aelf,root):
        if not root: return "[]"
        queue= collections.deque()
        queue.append(root)
        res=[]
        while queue:
            node=queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        return '[' +','.join(res)+']'
    
    def deserialize(self,data):
        if data== "[]" : return
        vals,i =data[1:-1].split(','),1
        root =TreeNode(int(vals[0]))
        queue=collections.deque()
        queue.append(root)
        while queue : 
            node =queue.popleft()
            if vals[i] != "null":
                node.left= TreeNode(int(vals[i]))
                queue.append(node.left)

            i+=1
            if vals[i] != "null":
                node.left= TreeNode(int(vals[i]))
                queue.append(node.right)

        return root 