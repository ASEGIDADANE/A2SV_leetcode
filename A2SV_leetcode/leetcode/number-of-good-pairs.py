class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        frequency = {}

        
        for num in nums:
            if num in frequency:
                count += frequency[num]
                frequency[num] += 1
            else:
                frequency[num] = 1

        return count
        
         
         
        