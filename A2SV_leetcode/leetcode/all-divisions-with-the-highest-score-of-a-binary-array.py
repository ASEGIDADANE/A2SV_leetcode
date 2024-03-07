class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = sum(nums)
        zeros = 0
        lis = [ones]

        for i in nums:
            if i == 0:
               zeros +=1
            else:
                ones -= 1
            lis.append(ones + zeros)
        max_ = max(lis)
        return [score for score in range(len(lis)) if lis[score] == max_]
       
    

        

