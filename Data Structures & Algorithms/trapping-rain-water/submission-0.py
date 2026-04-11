class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        water = 0
        lmax=rmax=-1
        while(l<r):
            lmax = max(lmax,height[l])
            rmax = max(rmax,height[r])
            if lmax<rmax:
                water+=min(lmax,rmax)-height[l]
                l+=1
            else:
                water+=min(lmax,rmax)-height[r]
                r-=1
        return water
