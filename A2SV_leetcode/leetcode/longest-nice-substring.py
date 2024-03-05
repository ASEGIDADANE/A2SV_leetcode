class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest_substring = ""

        def is_nice(substring):
            for char in substring:
                if char.lower() not in substring or char.upper() not in substring:
                    return False
            return True

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if is_nice(substring) and len(substring) > len(longest_substring):
                    longest_substring = substring

        return longest_substring

        

        

        