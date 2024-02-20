class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x: x[1])
        print(points)
        count = 0
        arrow=0
        for start,end in points:
            if count==0 or start>arrow:
                count+=1
                arrow=end
        return count
        

            
        