class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x = bisect_left(nums,target)
        print(x)
        y = bisect_right(nums,target)
        print(y)
        if x == y :
            return [-1,-1]
        if len(nums) == 1 and nums[0]!=target:
            return [-1,-1]
        return [x,y-1]