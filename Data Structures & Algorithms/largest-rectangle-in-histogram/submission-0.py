class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left,right=[-1]*n,[n]*n
        max_ar = 0
        stack=[]
        for i in range(n):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            left[i]=stack[-1] if stack else -1
            stack.append(i)

        stack.clear()
        for i in range(n-1,-1,-1):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i]*(right[i]-left[i]-1))

        return max_area