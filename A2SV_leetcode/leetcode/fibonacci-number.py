class Solution:
    def fib(self, n: int) -> int:
        lis=[0,1]
        if n==1:
            return 1
        if n==0:
            return 0
        if n>=2:
            for i in range(2,n+1):
                sumx=lis[-1]+lis[-2]
                lis.append(sumx)
                print(lis)

            return lis[-1]


        
        