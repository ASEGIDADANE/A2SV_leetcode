# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        
        def travers(root,col,row):
            if root:
                ans.append([col,row,root.val])
                travers(root.left,col-1,row+1)
                travers(root.right,col+1,row+1)
            return
        travers(root,0,0)
        ans.sort()
        print(ans)
        d=defaultdict(list)
        for i,j,k in ans:
            d[i].append(k)
        print(d)
        return list(d.values())

         
                
            













        