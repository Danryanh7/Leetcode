# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = []
        if not root:
            return res
        q.append(root)
        q.append(None)
        temp = []
        while q:
            node = q.pop(0)
            if (node == None):
                res.append(temp)
                temp = []
                q.append(None)
                if q[0] == None:
                    break
                continue
            temp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
            
            
            