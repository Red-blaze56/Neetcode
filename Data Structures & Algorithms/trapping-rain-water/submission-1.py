class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        NLHR = [0]*n
        PSHL = [0]*n
        PreMax,SufMax,water=0,0,0
        for i in range(n):
            PreMax = max(PreMax,height[i])
            NLHR[i] = PreMax
        for i in range(n-1,-1,-1):
            SufMax = max(SufMax,height[i])
            PSHL[i] = SufMax
        for i in range(n):
            water+=min(NLHR[i],PSHL[i])-height[i]
        return water