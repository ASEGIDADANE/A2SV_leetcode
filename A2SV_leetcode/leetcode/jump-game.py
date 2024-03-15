class Solution:
    def canJump(self, nums: List[int]) -> bool:
        intial = 0
        for n in nums:
            if intial < 0:
                return False
            elif n > intial:
               intial =n
            intial -= 1
            
        return True
        

        