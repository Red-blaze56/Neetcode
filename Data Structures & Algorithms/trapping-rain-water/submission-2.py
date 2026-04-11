class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        leftmax,rightmax=-1,-1
        water = 0
        while l<r:
            leftmax = max(leftmax,height[l])
            rightmax = max(rightmax,height[r])
            if leftmax<rightmax:
                water += min(leftmax,rightmax) - height[l]
                l+=1
            else:
                water += min(leftmax,rightmax) - height[r]
                r-=1
        return water