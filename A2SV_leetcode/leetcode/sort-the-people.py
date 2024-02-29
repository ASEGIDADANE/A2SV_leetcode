class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping=zip(heights,names)
        list1=[]
        for i,j in sorted(mapping):
            list1.append(j)
        return list1[::-1]
    