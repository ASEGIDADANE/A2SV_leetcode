class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        lis=[]
        for i in range(1,len(weights)):
            lis.append(weights[i]+weights[i-1])
        lis.sort()
        mini=0
        maxi=0
        mini=sum(lis[:k-1])
        if k!=1:
            
            maxi=sum(lis[-k+1:])
       
        return maxi -mini

        