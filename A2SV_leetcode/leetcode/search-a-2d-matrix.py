class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])

        l=0
        r=n*m-1
        while l<=r:
            mid=l +(r-l)//2
            number=matrix[mid//n][mid%n]
            if number<target:
                l=mid+1
            elif number >target:
                r=mid-1
            else:
                return True
        return False



           




