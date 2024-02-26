class Solution:
    def getRow(self, n: int) -> List[int]:
        
        res = [[1], [1, 1]]
        if n < 2:
            return res[n]

        for i in range(2, n + 1):
            row = [1] 

            for j in range(1, i):
                row.append(res[i - 1][j - 1] + res[i - 1][j])
              

            row.append(1)  
            res.append(row)

        return res[n]