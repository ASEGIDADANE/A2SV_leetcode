class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=max(nums)
        best=-1
        while left <= right:
            mid=left + (right - left)//2
            divisor=0
            for num in nums:
                divisor+=ceil(num/mid)
            if divisor > threshold:
                left=mid+1
               
                
            else:
                right=mid-1
                best=mid
                
               
               
        return best

                
