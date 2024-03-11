class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum_val = roman[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if roman[s[i]] < roman[s[i + 1]]:
                sum_val -= roman[s[i]]
            else:
                sum_val += roman[s[i]]
        return sum_val

           
        
        