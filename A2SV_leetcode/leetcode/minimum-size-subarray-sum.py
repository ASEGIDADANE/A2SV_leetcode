class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
       
        total=0
        min_lenght=float('inf')
        for r  in range(len(nums)):
            total+=nums[r]
            while total>=target:
                min_lenght=min(min_lenght,r-l+1)
                total-=nums[l]
                l+=1
        if min_lenght==float('inf'):
            return 0
        return min_lenght


        