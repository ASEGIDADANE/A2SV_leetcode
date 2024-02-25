class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        left=0
        right=len(p)-1
        res=[]
        
        p=Counter(p)
        print(p)

        while right <len(s):
            sub=s[left:right+1]
            sub=Counter(sub)
            print(p)
            if  sub==p:
                res.append(left)
            left+=1
            right+=1
        return res


        