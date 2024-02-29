class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ret = []
        
        # while there is still both, since will ignore everything that is not in.
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            interval = firstList[i]
            interval2 = secondList[j]
            
           
            if interval[0] > interval2[0]:
                start = interval[0]
            
            else:
                start = interval2[0]
                
          
            end = min(interval[1], interval2[1])
            
            if start <= end:
                ret.append([start, end])
            
           
            if end == interval[1]:
                i += 1
                
            
            if end == interval2[1]:
                j += 1
                
        return ret
        
        