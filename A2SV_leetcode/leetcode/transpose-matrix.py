class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])
        ans=[[0]*n for _ in range(m)]
        print(ans)
        for i in range(m):
            for j in range(n):
                ans[i][j]=matrix[j][i]
        return ans        