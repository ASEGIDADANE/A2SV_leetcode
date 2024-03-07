class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right,best=max(weights),sum(weights),-1
        while left <=right:
            mid=left +(right -left)//2
            day=1
            weight=0
            for i in range(len(weights)):
              weight+=weights[i]
              if weight >mid:
                  day+=1
                  weight=weights[i]


            if day > days:
                left =mid+1
            else:
                right=mid-1
                best=mid
        return best
                
