class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenght=0
        list1=[]
        max_lenght=lenght
        for i in range(len(s)):
            list1.append(s[i])
            if len(set(list1))==len(list1):
                max_lenght=max(lenght,len(list1))

            else:
                list1.remove(list1[0])
        return max_lenght
        
        