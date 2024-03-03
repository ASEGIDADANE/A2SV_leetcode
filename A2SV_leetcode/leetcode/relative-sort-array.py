class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        list1=[]
        for x in arr2:
            while x in arr1:
                list1.append(x)
                arr1.remove(x)
        return list1+sorted(arr1)

        