class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        lenght = 0
        count = 0
        from collections import defaultdict
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        for val in dict.values():
            if val % 2 == 0:
                lenght += val
            if val%2==1:
                lenght+=val-1
        if len(s)>lenght:
            lenght+=1
            
    
        return lenght
  







        