class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        poi1=0
        poi2=0
        lis=[]
        while poi1<len(nums1) and poi2 <len(nums2):
            if nums1[poi1]<nums2[poi2]:
                poi1+=1
            elif nums1[poi1]==nums2[poi2]:
               
                x=nums1[poi1]
                lis.append(x)
                poi1+=1
                poi2+=1
            elif nums1[poi1]>nums2[poi2]:
                poi2+=1
        print(lis)

        return lis





        