# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums==[]:
            return None
        max_=max(nums)
        indx=nums.index(max_)
        root=TreeNode(max_)
        root.left=self.constructMaximumBinaryTree(nums[:indx])
        root.right=self.constructMaximumBinaryTree(nums[indx+1:])
        return root
        
       

