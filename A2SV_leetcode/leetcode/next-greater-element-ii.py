class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[-1]*len(nums)
        for i in range(2):
            for i in range(len(nums)):
                while stack and nums[stack[-1]]<nums[i]:
                    indx=stack.pop()
                    res[indx]=nums[i]
                
                stack.append(i)
                
        return res