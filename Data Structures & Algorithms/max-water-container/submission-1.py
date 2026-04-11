class Solution:
    def maxArea(self, height):
        l, r = 0, len(height)-1
        max_area = 0
        while l<r:
            b = r-l
            h = min(height[l],height[r])
            ar = b*h
            max_area = max(max_area,ar)
            if height[l]<height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
            else:
                l+=1
                r-=1
        return max_area