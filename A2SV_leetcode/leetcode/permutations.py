class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def bactracking(nums,start,perm):
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in perm:
                    perm.append(nums[i])
                    bactracking(nums,i+1,perm)
                    perm.pop()
            
        bactracking(nums,0,[])
        return res
        