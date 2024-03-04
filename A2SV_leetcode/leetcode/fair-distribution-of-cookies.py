class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.max_=float('inf')

        def cookies_(dis,indx):
            if indx == len(cookies):
                self.max_=min(self.max_,max(dis))
                return 
            for i in range(k):
                # for j in range(len(cookies)):
                    dis[i]+=cookies[indx]
                    if dis[i]<=self.max_:
                        cookies_(dis,indx+1)
                    dis[i]-=cookies[indx]
                    

        dis=[0]*k
        cookies_(dis,0)
        return self.max_
        