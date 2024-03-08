from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i=0
        count = defaultdict(int) 
        for j in range(len(fruits)):
            count[fruits[j]] += 1 
            if len(count) > 2: 
                count[fruits[i]] -= 1 
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1 
        return j - i + 1


        