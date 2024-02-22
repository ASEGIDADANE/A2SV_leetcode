class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        length = float('inf')
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target and l <= r:
                length = min(length, r - l + 1)
                total -= nums[l]
                l += 1
        if length == float('inf'):
            return 0
        return length