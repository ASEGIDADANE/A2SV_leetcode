class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs.sort()
        count=0
        sum_=0
        for i in range(len(costs)):
            sum_+=costs[i]

            if sum_ <= coins:
                count+=1
            else:
                sum_-=costs[i]

        return count
               

