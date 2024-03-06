class Solution:
    def findMin(self, n: List[int]) -> int:
        left,right= 0, len(n)-1
        while left<=right:
            mid = (left+right)//2

            if n[right]<n[left]:
                if n[mid]>n[right]:
                    left = mid+1
                else:
                    right = mid
            else:
                break
        return n[left]