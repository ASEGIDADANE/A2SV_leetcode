class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        resu=""
        for char in s:
            if char.isalnum():
                resu+=char
        return resu==resu[::-1]
        