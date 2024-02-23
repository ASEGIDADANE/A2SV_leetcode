class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        dict = {}
    
        for num in nums2:
            while len(st) != 0 and num > st[-1]:
                dict[st[-1]] = num
                st.pop()
            st.append(num)
    
        while len(st) != 0:
            dict[st[-1]] = -1
            st.pop()
    
        res = [0] * len(nums1)
        for i in range(len(nums1)):
            res[i] = dict[nums1[i]]
                                            
        return res
              
      
              
          



                

                
        