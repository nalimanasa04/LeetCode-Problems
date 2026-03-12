class DSU:
    def __init__(self,n):
        self.p=list(range(n))
        self.r=[0]*n
        self.c=n
    def find(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]
            x=self.p[x]
        return x
    def union(self,a,b):
        pa,pb=self.find(a),self.find(b)
        if pa==pb:
            return False
        if self.r[pa]<self.r[pb]:
            pa,pb=pb,pa
        self.p[pb]=pa
        if self.r[pa]==self.r[pb]:
            self.r[pa]+=1
        self.c-=1
        return True

class Solution:
    def maxStability(self,n,edges,k):
        def check(T):
            d=DSU(n)
            for u,v,s,m in edges:
                if m:
                    if s<T or not d.union(u,v):
                        return False
            need=[]
            free=[]
            for u,v,s,m in edges:
                if m:
                    continue
                if s>=T:
                    free.append((u,v))
                elif s*2>=T:
                    need.append((u,v))
            used=0
            for u,v in free:
                if d.union(u,v):
                    pass
            for u,v in need:
                if d.c==1:
                    break
                if used==k:
                    break
                if d.union(u,v):
                    used+=1
            return d.c==1
        lo,hi=0,200000
        ans=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if check(mid):
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        return ans