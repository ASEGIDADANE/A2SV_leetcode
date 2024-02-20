class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        close,open=0,0
        for i in s:
            if i=='(':
                open+=1
            else:
                if open!=0:
                    open-=1
                else:
                    close+=1
        return open+close