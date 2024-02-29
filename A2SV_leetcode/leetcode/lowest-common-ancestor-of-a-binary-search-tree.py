# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_ancestor(node,val1,val2):
            if not node:
                return
            if val1 > node.val and val2 < node.val:
                return node
            if val1 < node.val and val2 > node.val:
                return node
            if val1 == node.val or val2 == node.val:
                return node
            if val1 < node.val and val2 < node.val:
                return find_ancestor(node.left,val1,val2)
            return find_ancestor(node.right,val1,val2)
        return find_ancestor(root,q.val,p.val)
        

       





         