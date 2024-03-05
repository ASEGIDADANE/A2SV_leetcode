class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        nums.sort()
        def subset_dub(start,path,nums):
            
            if path[:] not in res:

                res.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                
                
                subset_dub(i+1,path,nums)
                path.pop()
        subset_dub(0,[],nums)
        print(res.sort())
        return res
        

        


        