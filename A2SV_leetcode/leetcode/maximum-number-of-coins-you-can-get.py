class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort() 
        n = len(piles)
        count = 0
        i = n - 2  
        res = 0
        while count != n // 3:
            res += piles[i]  
            i -= 2  
            count += 1  
        return res
