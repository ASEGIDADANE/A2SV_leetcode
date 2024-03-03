class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumx=0
        for i in range(len(mat)):
            sumx+=mat[i][i]
            sumx+=mat[i][len(mat)-1-i]
        if len(mat)%2==1:
            sumx-=mat[len(mat)//2][len(mat)//2]


        return sumx
        