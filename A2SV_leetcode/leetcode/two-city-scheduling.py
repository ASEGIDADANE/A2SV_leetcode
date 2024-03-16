class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        sum_=0

        s = sorted(costs, key=lambda x: x[0] - x[1])
        m=int(len(s)/2)
        for i in range(m):
            sum_+=s[i][0]
        for i in range(m,len(s)):
            sum_ += s[i][1]
        return sum_

        


       

        