class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def subset(nums,path,start):
            # if len(path)<=len(nums):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                subset(nums,path,i+1)
                path.pop()
        subset(nums,[],0)
        return res
        
        