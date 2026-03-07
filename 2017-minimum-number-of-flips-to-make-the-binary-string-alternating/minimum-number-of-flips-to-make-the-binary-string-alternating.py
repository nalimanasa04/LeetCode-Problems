class Solution:
    def minFlips(self, s: str) -> int:
        n=len(s)
        s=s+s
        a=b=""
        for i in range(len(s)):
            if i%2:
                a+="1"
                b+="0"
            else:
                a+="0"
                b+="1"
        res=float('inf')
        da=db=0
        l=0
        for r in range(len(s)):
            if s[r]!=a[r]: da+=1
            if s[r]!=b[r]: db+=1
            if r-l+1>n:
                if s[l]!=a[l]: da-=1
                if s[l]!=b[l]: db-=1
                l+=1
            if r-l+1==n:
                res=min(res,da,db)
        return res