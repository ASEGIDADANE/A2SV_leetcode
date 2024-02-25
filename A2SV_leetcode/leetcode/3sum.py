class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,a in enumerate(nums):

            if i>0 and a== nums[i -1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l<r:
                sum_tripel=a+nums[l]+nums[r]
                if sum_tripel<0:
                    l+=1
                elif sum_tripel>0:
                    r-=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while  l<r and nums[l]==nums[l-1]:
                        l+=1
        return res
        